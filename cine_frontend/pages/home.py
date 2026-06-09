# home.py

import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.components.carousel import carousel


def movie_card(titulo, genero, clasificacion, ruta):
    return rx.card(
        rx.vstack(

            rx.link(
                rx.image(
                    src=ruta,
                    width="220px",
                    height="340px",
                    border_radius="10px",
                    object_fit="cover",
                ),
                href="/pelicula",
            ),

            rx.heading(
                titulo,
                size="4",
                text_align="center",
                min_height="65px",
            ),

            rx.badge(
                genero,
                color_scheme="blue",
            ),

            rx.badge(
                clasificacion,
                color_scheme="red",
            ),

            rx.button(
                "Ver detalles",
                width="100%",
            ),

            spacing="3",
            align="center",
        ),
        width="270px",
    )


def peliculas_section():
    return rx.vstack(
        rx.heading(
            "──────────────── EN CARTELERA ────────────────",
            size="6",
            color="white",
        ),

        rx.flex(

            movie_card(
                "Scary Movie 6",
                "Comedia",
                "R/14",
                "/Imagenes/posters/scarymovie6.jpg",
            ),

            movie_card(
                "El Diablo Viste de Prada 2",
                "Comedia",
                "R/14",
                "/Imagenes/posters/prada2.jpg",
            ),

            movie_card(
                "El Mandaloriano y Grogu",
                "Ciencia Ficción",
                "R/14",
                "/Imagenes/posters/grogu.jpg",
            ),

            movie_card(
                "Mortal Kombat II",
                "Acción",
                "R/18",
                "/Imagenes/posters/mortalkombat2.jpg",
            ),

            movie_card(
                "Supergirl",
                "Acción",
                "R/14",
                "/Imagenes/posters/supergirl.jpg",
            ),

            movie_card(
                "Toy Story 5",
                "Animación",
                "ATP",
                "/Imagenes/posters/toystory5.jpg",
            ),

            movie_card(
                "Moana",
                "Aventura",
                "ATP",
                "/Imagenes/posters/moana.jpg",
            ),

            movie_card(
                "Spider-Man: Brand New Day",
                "Acción",
                "R/14",
                "/Imagenes/posters/spiderman.jpg",
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
            "PRÓXIMAMENTE",
            size="8",
            color="white",
        ),

        rx.text("Dune: Part Three", color="white"),
        rx.text("The Batman II", color="white"),
        rx.text("Avengers: Secret Wars", color="white"),
        rx.text("Frozen 3", color="white"),

        spacing="3",
        padding="2em",
    )


def footer():
    return rx.center(
        rx.text(
            "© 2026 MovieTime RD - Todos los derechos reservados"
        ),
        width="100%",
        padding="1.5em",
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
    )
