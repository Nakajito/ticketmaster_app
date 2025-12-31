import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.heading("🎫 EventFinder México 🎫", size="9", margin_bottom="0.5em"),
        rx.text(
            "Encuentra los mejores eventos en tu ciudad.",
            color="gray",
            margin_bottom="1.5em",
            text_align="center",
        ),
    )
