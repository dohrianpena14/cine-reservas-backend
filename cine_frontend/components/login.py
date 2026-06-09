import reflex as rx

from cine_frontend.components.navbar import navbar


def login():
    return rx.vstack(
        navbar(),

        rx.heading("Iniciar Sesión", size="8"),

        rx.input(
            placeholder="Correo electrónico",
            width="350px",
        ),

        rx.input(
            placeholder="Contraseña",
            type="password",
            width="350px",
        ),

        rx.link(
            "¿Olvidaste tu contraseña?",
            href="#",
        ),

        rx.button(
            "Iniciar Sesión",
            width="350px",
        ),

        rx.text("¿No tienes cuenta?"),

        rx.link(
            "Registrarse",
            href="/registrar",
        ),

        align="center",
        padding="3em",
    )