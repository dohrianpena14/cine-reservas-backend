import reflex as rx


def navbar():
    return rx.hstack(
        rx.heading("🎬 MovieTime RD", size="7"),
        rx.spacer(),
        rx.hstack(
            rx.text("Cartelera"),
            rx.text("Próximamente"),
            rx.text("Eventos"),
            rx.button("Iniciar Sesión"),
            spacing="6",
        ),
        width="100%",
        padding="1em",
        bg="#0f172a",
        color="white",
    )


def hero():
    return rx.center(
        rx.vstack(
            rx.heading("La mejor experiencia de cine", size="9"),
            rx.text(
                "Reserva tus entradas de forma rápida y sencilla.",
                size="5",
            ),
            rx.button("Ver Cartelera", size="3"),
            spacing="5",
        ),
        height="500px",
        bg="linear-gradient(to right, #111827, #1e293b)",
        color="white",
    )


def peliculas():
    return rx.vstack(
        rx.heading("🎥 Reproduciendo Ahora", size="7"),
        rx.hstack(
            rx.card(rx.text("Lilo & Stitch")),
            rx.card(rx.text("Misión Imposible")),
            rx.card(rx.text("Minecraft")),
            rx.card(rx.text("Karate Kid")),
            spacing="4",
        ),
        padding="2em",
    )


def index():
    return rx.vstack(
        navbar(),
        hero(),
        peliculas(),
        width="100%",
        spacing="0",
    )


app = rx.App()
app.add_page(index)