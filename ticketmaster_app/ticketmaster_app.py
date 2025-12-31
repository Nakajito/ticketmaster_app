import reflex as rx
import requests
import os
from dotenv import load_dotenv
from typing import List, Dict, Any
from components.ciudades import CIUDADES_MX
from components.search_events import search_events
from components.process_events import _process_events
from components.event_card import event_card
from components.start_new_search import start_new_search
from components.paginacion import next_page, prev_page

from components.header import header

load_dotenv()

API_KEY = os.getenv("TICKETMASTER_API_KEY")

CIUDADES_MX = CIUDADES_MX


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

    # Importada desde components/paginacion.py
    next_page = next_page
    prev_page = prev_page

    # Importada desde components/search_events.py
    search_events = search_events

    # Importada desde components/start_new_search.py
    start_new_search = start_new_search

    # Importada desde components/process_events.py
    _process_events = _process_events

    # Importada desde components/event_card.py
    event_card = event_card


def index():
    return rx.container(
        rx.vstack(
            header(),
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
