import reflex as rx


def navbar():
    return rx.hstack(
        rx.heading(
            "🎬 MovieTime RD",
            size="7"
        ),

        rx.spacer(),

        rx.hstack(
            rx.link("Inicio", href="/"),
            rx.link("Cartelera", href="/cartelera"),
            rx.link("Próximamente", href="/proximamente"),
            rx.link("Eventos", href="/eventos"),
            spacing="6",
        ),

        rx.spacer(),

        rx.hstack(
            rx.button("Iniciar Sesión"),
            rx.button("Registrarse"),
            spacing="3",
        ),

        width="100%",
        padding="1em",
        bg="#111827",
        color="white",
    )