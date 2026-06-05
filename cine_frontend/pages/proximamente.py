import reflex as rx
from cine_frontend.components.navbar import navbar

def proximamente():
    return rx.vstack(
        navbar(),
        rx.heading("Próximamente", size="8"),
        rx.text("Aquí aparecerán los próximos estrenos."),
        padding="2em",
    )