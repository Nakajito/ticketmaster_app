import reflex as rx


def _process_events(self, events_data):
    processed = []
    for event in events_data:
        # Obtener Imagen
        images = event.get("images", [])
        image_url = images[0]["url"] if images else "https://via.placeholder.com/300"

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
