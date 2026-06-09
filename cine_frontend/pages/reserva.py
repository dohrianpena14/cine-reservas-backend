import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.components.seats import seats


def reserva():
    return rx.vstack(

        navbar(),

        rx.heading(
            "Reservar Entradas",
            size="8",
            color="white",
        ),

        seats(),

        rx.select(
            ["2:00 PM", "5:00 PM", "8:00 PM"],
            placeholder="Seleccione horario",
            width="300px",
        ),

        rx.select(
            ["1", "2", "3", "4", "5"],
            placeholder="Cantidad de boletos",
            width="300px",
        ),

        rx.button(
            "Confirmar Reserva",
            size="4",
            color_scheme="green",
        ),

        bg="#0f172a",
        color="white",
        min_height="100vh",
        width="100%",
        align="center",
        padding_bottom="4em",
    )