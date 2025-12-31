import reflex as rx
import requests
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

API_KEY = os.getenv("TICKETMASTER_API_KEY")

# --- LISTA DE CIUDADES VÁLIDAS ---
CIUDADES_MX = [
    "Todas las ciudades",
    "Ciudad de Mexico",
    "Monterrey",
    "Guadalajara",
]


class State(rx.State):
    events: List[Dict[str, Any]] = []
    search_query: str = ""
    city_filter: str = ""
    category_filter: str = ""
    is_loading: bool = False
    error_message: str = ""
    page: int = 0  # Empezamos en la página 0

    def handle_search_change(self, value: str):
        self.search_query = value

    def set_city_filter(self, value: str):
        self.city_filter = value

    def set_category_filter(self, value: str):
        self.category_filter = value

    def next_page(self):
        """Avanza a la siguiente página"""
        self.page += 1
        return self.search_events()

    def prev_page(self):
        """Regresa a la página anterior"""
        if self.page > 0:
            self.page -= 1
            return self.search_events()

    def search_events(self):
        self.is_loading = True
        self.error_message = ""
        self.events = []
        yield

        try:
            url = "https://app.ticketmaster.com/discovery/v2/events.json"

            params = {
                "apikey": API_KEY,
                "size": 12,  # 12 resutlados por página para que cargue rápido
                "page": self.page,  # <--- LE DECIMOS A LA API QUÉ PÁGINA QUEREMOS
                "sort": "date,asc",
                "countryCode": "MX",
            }

            if self.search_query.strip():
                params["keyword"] = self.search_query

            # Solo enviamos el parámetro 'city' si:
            # 1. Hay algo seleccionado.
            # 2. Y LO QUE SELECCIONARON NO ES "Todas las ciudades"
            if self.city_filter.strip() and self.city_filter != "Todas las ciudades":
                params["city"] = self.city_filter

            if self.category_filter and self.category_filter != "Todas":
                params["classificationName"] = self.category_filter

            # Debug para verificar
            # print(f"Enviando params: {params}")

            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if "_embedded" in data and "events" in data["_embedded"]:
                raw_events = data["_embedded"]["events"]
                self.events = self._process_events(raw_events)
            else:
                self.error_message = "No se encontraron eventos con esos filtros."

        except Exception as e:
            self.error_message = f"Error: {str(e)}"
        finally:
            self.is_loading = False

    def start_new_search(self):
        """Llamar a esta función desde el botón BUSCAR en lugar de search_events directo"""
        self.page = 0  # Reseteamos a la primera página
        return self.search_events()

    def _process_events(self, events_data):
        processed = []
        for event in events_data:
            # Obtener Imagen
            images = event.get("images", [])
            image_url = (
                images[0]["url"] if images else "https://via.placeholder.com/300"
            )

            # Obtener Ubicación
            venues = event.get("_embedded", {}).get("venues", [{}])
            venue_name = venues[0].get("name", "Ubicación desconocida")
            city = venues[0].get("city", {}).get("name", "")

            # Lógica de DISPONIBILIDAD
            # Ticketmaster usa 'dates.status.code' para decir si está activo
            status_code = (
                event.get("dates", {}).get("status", {}).get("code", "unknown").lower()
            )

            is_available = False
            status_text = "No disponible"
            status_color = "gray"

            if status_code == "onsale":
                is_available = True
                status_text = "Disponible"
                status_color = "green"
            elif status_code == "cancelled":
                status_text = "Cancelado"
                status_color = "red"
            elif status_code == "rescheduled" or status_code == "postponed":
                status_text = "Posponido"
                status_color = "orange"

            # Lógica de PRECIO
            price_ranges = event.get("priceRanges", [])

            if price_ranges:
                # Si la API da precios, los usamos
                min_p = price_ranges[0].get("min", 0)
                curr = price_ranges[0].get("currency", "MXN")
                price_text = f"Desde ${min_p} {curr}"
            elif is_available:
                # Si está disponible pero no da precio, mostramos esto:
                price_text = "Ver precio en web"
            else:
                price_text = "Agotado / No disponible"

            processed.append(
                {
                    "name": event.get("name"),
                    "date": event.get("dates", {})
                    .get("start", {})
                    .get("localDate", "Por confirmar"),
                    "image": image_url,
                    "venue": f"{venue_name}, {city}",
                    "price": price_text,  # Texto del precio
                    "status": status_text,  # Texto del estatus
                    "status_color": status_color,  # Color para la UI
                    "url": event.get("url"),
                }
            )
        return processed


def event_card(event: Dict[str, Any]):
    return rx.card(
        rx.inset(
            rx.image(
                src=event["image"],
                width="100%",
                height="150px",
                object_fit="cover",
            ),
            side="top",
            pb="current",
        ),
        rx.vstack(
            # Fila superior con Fecha y Estatus
            rx.hstack(
                rx.badge(event["date"], color_scheme="violet", variant="soft"),
                rx.spacer(),
                rx.badge(
                    event["status"], color_scheme=event["status_color"], variant="solid"
                ),
                width="100%",
            ),
            rx.heading(event["name"], size="3", trim="both"),
            rx.text(event["venue"], size="1", color="gray"),
            # Sección de precio destacada
            rx.text(event["price"], size="2", weight="bold"),
            rx.link(
                rx.button(
                    "Ir a Ticketmaster",
                    width="100%",
                    variant="surface",
                    cursor="pointer",
                ),
                href=event["url"],
                is_external=True,
                width="100%",
            ),
            spacing="2",
        ),
        width="100%",
    )


def index():
    return rx.container(
        rx.vstack(
            rx.heading("🎫 EventFinder México", size="8", margin_bottom="0.5em"),
            rx.text(
                "Encuentra los mejores eventos en tu ciudad.",
                color="gray",
                margin_bottom="1.5em",
            ),
            rx.flex(
                # Buscador de Texto
                rx.input(
                    placeholder="Artista o evento...",
                    on_change=State.handle_search_change,
                    width=["100%", "100%", "250px"],
                ),
                # SELECTOR DE CIUDADES
                rx.select(
                    CIUDADES_MX,
                    placeholder="Selecciona Ciudad",
                    default_value="Todas las ciudades",  # Puedes poner esto por defecto si quieres
                    on_change=State.set_city_filter,
                    width=["100%", "100%", "200px"],
                ),
                # Selector de Categoría
                rx.select(
                    ["Todas", "Music", "Sports", "Arts & Theatre", "Family"],
                    placeholder="Categoría",
                    on_change=State.set_category_filter,
                    width=["100%", "100%", "180px"],
                ),
                # Botón Buscar
                rx.button(
                    rx.icon("search"),
                    "Buscar",
                    on_click=State.search_events,
                    loading=State.is_loading,
                    width=["100%", "100%", "auto"],
                ),
                spacing="3",
                flex_wrap="wrap",
                width="100%",
                justify="center",
            ),
            rx.cond(
                State.error_message != "",
                rx.callout(
                    State.error_message, icon="triangle_alert", color_scheme="red"
                ),
            ),
            rx.divider(margin_y="2em"),
            rx.grid(
                rx.foreach(State.events, event_card),
                columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
                spacing="4",
                width="100%",
            ),
            rx.hstack(
                rx.button(
                    "Anterior",
                    on_click=State.prev_page,
                    disabled=State.page == 0,  # Desactivar si estamos en la pag 0
                    variant="soft",
                ),
                rx.text(f"Página {State.page + 1}", weight="bold"),
                rx.button("Siguiente", on_click=State.next_page, variant="soft"),
                spacing="4",
                margin_top="2em",
                justify="center",
                width="100%",
            ),
            align="center",
            padding_top="4em",
            padding_bottom="4em",
        )
    )


app = rx.App(theme=rx.theme(appearance="dark", accent_color="violet"))
app.add_page(index, title="EventFinder MX")
