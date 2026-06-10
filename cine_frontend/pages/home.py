import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.components.carousel import carousel
from cine_frontend.states.movie_state import MovieState


def movie_card(movie):

    return rx.card(
        rx.vstack(

            rx.image(
                src=f"/Imagenes/posters/{movie['imagen_url']}",
                width="220px",
                height="340px",
                border_radius="10px",
                object_fit="cover",
            ),

            rx.heading(
                movie["titulo"],
                size="4",
                text_align="center",
                color="white",
            ),

            rx.badge(
                movie["genero"],
                color_scheme="blue",
            ),

            rx.badge(
                movie["clasificacion"],
                color_scheme="red",
            ),

            rx.text(
                f"RD${movie['precio']}",
                color="white",
            ),

            rx.link(
                rx.button(
                    "Ver detalles",
                    width="100%",
                    color_scheme="blue",
                ),
                href="/pelicula?id=" + movie["id"].to_string(),
            ),

            spacing="3",
            align="center",
        ),

        width="270px",
        bg="#1e293b",
    )


def peliculas_section():

    return rx.vstack(

        rx.heading(
            "──────────────── EN CARTELERA ────────────────",
            size="6",
            color="white",
        ),

        rx.flex(

            rx.foreach(
                MovieState.peliculas,
                movie_card,
            ),

            wrap="wrap",
            spacing="5",
            justify="center",
        ),

        width="100%",
        padding="2em",
        align="center",
    )


def proximamente_section():

    return rx.vstack(

        rx.heading(
            "──────────────── PRÓXIMAMENTE ────────────────",
            size="6",
            color="white",
            text_align="center",
        ),

        rx.text(
            "Dune: Part Three",
            color="white",
            text_align="center",
        ),

        rx.text(
            "The Batman II",
            color="white",
            text_align="center",
        ),

        rx.text(
            "Avengers: Secret Wars",
            color="white",
            text_align="center",
        ),

        rx.text(
            "Frozen 3",
            color="white",
            text_align="center",
        ),

        spacing="3",
        padding="2em",
        align="center",
        width="100%",
    )


def footer():

    return rx.vstack(

        rx.text(
            "© 2026 MovieTime RD - Todos los derechos reservados"
        ),

        spacing="4",
        align="center",
        width="100%",
        padding="2em",
        bg="#08132b",
        color="white",
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
        bg="#0f172a",
        min_height="100vh",

        on_mount=MovieState.cargar_peliculas,
    )