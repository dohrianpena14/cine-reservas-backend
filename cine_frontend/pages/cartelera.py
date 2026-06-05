import reflex as rx
from cine_frontend.components.navbar import navbar


def cartelera():
    return rx.vstack(
        navbar(),

        rx.heading(
            "🎥 Cartelera",
            size="8"
        ),

        rx.hstack(
            rx.card(
                rx.heading("Lilo & Stitch"),
                rx.text("Disponible"),
                width="250px",
            ),

            rx.card(
                rx.heading("Misión Imposible"),
                rx.text("Disponible"),
                width="250px",
            ),

            rx.card(
                rx.heading("Minecraft"),
                rx.text("Disponible"),
                width="250px",
            ),

            spacing="4",
        ),

        padding="2em",
    )