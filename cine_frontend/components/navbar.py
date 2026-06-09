import reflex as rx


def nav_link(texto, ruta):
    return rx.link(
        texto,
        href=ruta,
        color="white",
        text_decoration="none",
        padding="10px 16px",
        border_radius="8px",
        font_weight="600",

        _hover={
            "bg": "#374151",
        },

        _active={
            "bg": "#2563eb",
            "transform": "scale(0.97)",
        },
    )


def navbar():
    return rx.hstack(

        # Logo
        rx.link(
            rx.image(
                src="/Imagenes/MovieTime.png",
                height="110px",
            ),
            href="/",
        ),

        rx.spacer(),

        # Menú principal
        rx.hstack(
            nav_link("Inicio", "/"),
            nav_link("Próximamente", "/proximamente"),
            nav_link("Eventos", "/eventos"),
            spacing="5",
        ),

        rx.spacer(),

        # Menú usuario
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    "👤",
                    size="3",
                    border_radius="999px",
                    bg="#1f2937",
                    _hover={"bg": "#374151"},
                )
            ),

            rx.menu.content(

                rx.link(
                    "Iniciar Sesión",
                    href="/login",
                    width="100%",
                ),

                rx.separator(),

                rx.link(
                    "Registrarse",
                    href="/registrar",
                    width="100%",
                ),
            ),
        ),

        width="100%",
        height="100px",
        padding="0 2em",
        bg="#111827",
        color="white",
        align="center",
        position="sticky",
        top="0",
        z_index="1000",
    )