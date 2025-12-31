import reflex as rx
from typing import Dict, Any


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
