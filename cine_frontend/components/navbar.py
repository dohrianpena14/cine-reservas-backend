import reflex as rx


def nav_link(texto, ruta):
    return rx.link(
        texto,
        href=ruta,
        color="white",
        text_decoration="none",
        padding="8px 14px",
        border_radius="8px",
        _hover={"bg": "#374151"},
    )


def navbar():
    return rx.hstack(
        rx.image(
            src="/Imagenes/MovieTime.png",
            height="95px",
        ),

        rx.spacer(),

        rx.hstack(
            nav_link("Inicio", "/"),
            nav_link("Próximamente", "/proximamente"),
            nav_link("Eventos", "/eventos"),
            spacing="5",
        ),

        rx.spacer(),

        rx.menu.root(
            rx.menu.trigger(
                rx.button("👤")
            ),
            rx.menu.content(
                rx.link("Iniciar Sesión", href="/login"),
                rx.link("Registrarse", href="/registrar"),
            ),
        ),

        width="100%",
        height="90px",
        padding="0 2em",
        bg="#111827",
        color="white",
        align="center",
    )