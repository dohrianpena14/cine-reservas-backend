import reflex as rx

from cine_frontend.components.navbar import navbar


def registrar():
    return rx.vstack(
        navbar(),

        rx.heading(
            "Regístrate",
            size="8",
        ),

        rx.input(
            placeholder="Nombre completo",
            width="350px",
        ),

        rx.input(
            placeholder="Correo electrónico",
            width="350px",
        ),

        rx.input(
            placeholder="Contraseña",
            type="password",
            width="350px",
        ),

        rx.input(
            placeholder="Confirmar contraseña",
            type="password",
            width="350px",
        ),

        rx.button(
            "Registrarse",
            width="350px",
        ),

        rx.divider(),

        rx.heading(
            "¿Eres un cliente existente?",
            size="5",
        ),

        rx.text(
            "Usted tiene una cuenta/membresía en el cine. Haga clic aquí para acceder."
        ),

        rx.link(
            "Iniciar Sesión",
            href="/login",
        ),

        align="center",
        padding="3em",
    )