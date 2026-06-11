import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.data.movies import movies


class PeliculaState(rx.State):
    pelicula_id: str = "1"

    def cargar_pelicula(self):
        try:
            self.pelicula_id = self.router.page.params.get("id") or "1"
        except:
            self.pelicula_id = "1"


def pelicula_card(movie):
    return rx.hstack(

        rx.image(
            src=movie["poster"],
            width="320px",
            border_radius="12px",
        ),

        rx.vstack(
            rx.heading(movie["titulo"], size="8", color="white"),

            rx.badge(
                movie["genero"],
                color_scheme="blue",
            ),

            rx.badge(
                movie["clasificacion"],
                color_scheme="red",
            ),

            rx.text(
                f"Duración: {movie['duracion']}",
                color="white",
            ),

            rx.text(
                f"Director: {movie['director']}",
                color="white",
            ),

            rx.heading(
                "Sinopsis",
                size="5",
                color="white",
            ),

            rx.text(
                movie["sinopsis"],
                color="white",
            ),

            rx.heading(
                "Reparto",
                size="5",
                color="white",
            ),

            rx.vstack(
                *[
                    rx.text(actor, color="white")
                    for actor in movie["reparto"]
                ],
                spacing="1",
                align="start",
            ),

            rx.link(
                rx.button(
                    "Ver Trailer",
                    color_scheme="red",
                ),
                href=movie["trailer"],
                is_external=True,
            ),

           rx.link(
                rx.button(
                    "Reservar",
                    color_scheme="green",
                ),
                href=f"/reserva?pelicula={movie['id']}",
            ),

            align="start",
            spacing="3",
        ),

        spacing="8",
    )


def pelicula():
    return rx.vstack(

        navbar(),

        rx.cond(
            PeliculaState.pelicula_id == "1",
            pelicula_card(movies[0]),

            rx.cond(
                PeliculaState.pelicula_id == "2",
                pelicula_card(movies[1]),

                rx.cond(
                    PeliculaState.pelicula_id == "3",
                    pelicula_card(movies[2]),

                    rx.cond(
                        PeliculaState.pelicula_id == "4",
                        pelicula_card(movies[3]),

                        rx.cond(
                            PeliculaState.pelicula_id == "5",
                            pelicula_card(movies[4]),

                            rx.cond(
                                PeliculaState.pelicula_id == "6",
                                pelicula_card(movies[5]),

                                rx.cond(
                                    PeliculaState.pelicula_id == "7",
                                    pelicula_card(movies[6]),
                                    pelicula_card(movies[7]),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),

        bg="#0f172a",
        min_height="100vh",
        width="100%",
        padding="2em",

        on_mount=PeliculaState.cargar_pelicula,
    )