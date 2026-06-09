import reflex as rx


def seat(asiento):
    return rx.button(
        asiento,
        width="50px",
        height="50px",
        bg="#2563eb",
        color="white",
        border_radius="8px",
    )


def seats():
    return rx.vstack(

        rx.heading(
            "Pantalla",
            size="7",
            color="white",
        ),

        rx.box(
            width="600px",
            height="8px",
            bg="white",
            border_radius="999px",
        ),

        rx.hstack(
            seat("A1"), seat("A2"), seat("A3"), seat("A4"),
            seat("A5"), seat("A6"), seat("A7"), seat("A8"),
            spacing="2",
        ),

        rx.hstack(
            seat("B1"), seat("B2"), seat("B3"), seat("B4"),
            seat("B5"), seat("B6"), seat("B7"), seat("B8"),
            spacing="2",
        ),

        rx.hstack(
            seat("C1"), seat("C2"), seat("C3"), seat("C4"),
            seat("C5"), seat("C6"), seat("C7"), seat("C8"),
            spacing="2",
        ),

        rx.hstack(
            seat("D1"), seat("D2"), seat("D3"), seat("D4"),
            seat("D5"), seat("D6"), seat("D7"), seat("D8"),
            spacing="2",
        ),

        spacing="4",
        align="center",
        padding="2em",
    )