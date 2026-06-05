import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(
                "🎬 Movie Time RD",
                size="9"
            ),

            rx.text(
                "Compra tus boletos de cine de forma rápida y sencilla.",
                size="5"
            ),

            rx.text(
                "Películas, funciones y selección de asientos desde una sola plataforma."
            ),

            rx.hstack(
                rx.button(
                    "Iniciar Sesión",
                    color_scheme="blue"
                ),
                rx.button(
                    "Registrarse",
                    color_scheme="green"
                ),
            ),

            spacing="6",
            align="center",
            justify="center",
            min_height="100vh"
        )
    )


app = rx.App()
app.add_page(index)
