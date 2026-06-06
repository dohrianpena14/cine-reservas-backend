import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.components.carousel import carousel


def peliculas_section():
    return rx.vstack(
        rx.heading(
            "En Cartelera",
            size="8",
        ),

        rx.flex(
            rx.card(
                rx.vstack(
                    rx.box(
                        width="220px",
                        height="320px",
                        bg="gray",
                        border_radius="10px",
                    ),
                    rx.heading("Mortal Kombat II", size="4"),
                    rx.button("Comprar Boletos"),
                    align="center",
                ),
                width="250px",
            ),

            rx.card(
                rx.vstack(
                    rx.box(
                        width="220px",
                        height="320px",
                        bg="gray",
                        border_radius="10px",
                    ),
                    rx.heading("The Devil Wears Prada 2", size="4"),
                    rx.button("Comprar Boletos"),
                    align="center",
                ),
                width="250px",
            ),

            rx.card(
                rx.vstack(
                    rx.box(
                        width="220px",
                        height="320px",
                        bg="gray",
                        border_radius="10px",
                    ),
                    rx.heading("The Mandalorian & Grogu", size="4"),
                    rx.button("Comprar Boletos"),
                    align="center",
                ),
                width="250px",
            ),

            wrap="wrap",
            spacing="5",
            justify="center",
        ),

        padding="2em",
        width="100%",
    )


def proximamente_section():
    return rx.vstack(
        rx.heading(
            "Próximamente",
            size="8",
        ),

        rx.text("Dune: Part Three"),
        rx.text("Toy Story 5"),
        rx.text("Supergirl"),
        rx.text("Moana"),
        rx.text("Spider-Man: Brand New Day"),

        align="center",
        padding="2em",
    )


def footer():
    return rx.center(
        rx.text(
            "© 2026 MovieTime RD - Todos los derechos reservados"
        ),
        bg="#0f172a",
        color="white",
        width="100%",
        padding="1.5em",
    )


def home():
    return rx.vstack(
        navbar(),

        carousel(),

        peliculas_section(),

        proximamente_section(),

        footer(),

        spacing="0",
        width="100%",
    )