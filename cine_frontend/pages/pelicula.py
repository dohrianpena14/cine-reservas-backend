import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.data.movies import movies


pelicula_actual = movies[0]


def pelicula():
    return rx.vstack(

        navbar(),

        rx.hstack(

            rx.image(
                src=pelicula_actual["poster"],
                width="320px",
                border_radius="12px",
            ),

            rx.vstack(

                rx.heading(
                    pelicula_actual["titulo"],
                    size="8",
                    color="white",
                ),

                rx.badge(
                    pelicula_actual["genero"],
                    color_scheme="blue",
                ),

                rx.badge(
                    pelicula_actual["clasificacion"],
                    color_scheme="red",
                ),

                rx.text(
                    f"Duración: {pelicula_actual['duracion']}",
                    color="white",
                ),

                rx.text(
                    f"Director: {pelicula_actual['director']}",
                    color="white",
                ),

                rx.heading(
                    "Sinopsis",
                    size="5",
                    color="white",
                ),

                rx.text(
                    pelicula_actual["sinopsis"],
                    color="white",
                ),

                rx.heading(
                    "Reparto",
                    size="5",
                    color="white",
                ),

                rx.foreach(
                    pelicula_actual["reparto"],
                    lambda actor: rx.text(actor, color="white")
                ),

                rx.link(
                    rx.button(
                        "Ver Trailer",
                        color_scheme="red",
                    ),
                    href=pelicula_actual["trailer"],
                    is_external=True,
                ),

                rx.link(
                    rx.button(
                        "Reservar",
                        color_scheme="green",
                    ),
                    href="/reserva",
                ),

                align="start",
                spacing="3",
            ),

            spacing="8",
        ),

        bg="#0f172a",
        min_height="100vh",
        width="100%",
        padding="2em",
    )