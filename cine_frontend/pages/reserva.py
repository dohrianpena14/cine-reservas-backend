import reflex as rx

from cine_frontend.components.navbar import navbar
from cine_frontend.components.seats import seats
from cine_frontend.states.reserva_api_state import ReservaApiState


def reserva():
    return rx.vstack(

        navbar(),

        rx.heading(
            "Reservar Entradas",
            size="8",
            color="white",
        ),

        rx.text(
            "Seleccione el horario según la película elegida:",
            color="white",
        ),

        seats(),

        rx.radio(
            [
                "13:00:00 - Sala 2",
                "16:00:00 - Sala 2",
                "19:00:00 - Sala 2",
            ],
            direction="column",
            color_scheme="blue",
        ),

        rx.radio(
            ["1 boleto", "2 boletos", "3 boletos", "4 boletos", "5 boletos"],
            direction="row",
            color_scheme="green",
        ),

        rx.button(
            "Confirmar Reserva",
            size="4",
            color_scheme="green",
            on_click=ReservaApiState.reservar,
        ),

        rx.text(
            ReservaApiState.mensaje,
            color="yellow",
        ),
       
        bg="#0f172a",
        color="white",
        min_height="100vh",
        width="100%",
        align="center",
        padding_bottom="4em",
    )