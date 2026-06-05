import reflex as rx
from cine_frontend.components.navbar import navbar


def home():
    return rx.vstack(
        navbar(),

        rx.center(
            rx.vstack(
                rx.heading(
                    "Bienvenido a MovieTime RD",
                    size="9"
                ),

                rx.text(
                    "La mejor experiencia de cine en República Dominicana.",
                    size="5"
                ),

                rx.button(
                    "Ver Cartelera",
                    size="3"
                ),

                spacing="5",
            ),
            height="500px",
            width="100%",
        ),

        spacing="0",
    )