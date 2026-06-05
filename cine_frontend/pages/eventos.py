import reflex as rx
from cine_frontend.components.navbar import navbar

def eventos():
    return rx.vstack(
        navbar(),
        rx.heading("Eventos", size="8"),
        rx.text("Aquí aparecerán los eventos especiales."),
        padding="2em",
    )