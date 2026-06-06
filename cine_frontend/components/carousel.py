import reflex as rx


def carousel():
    return rx.box(
        rx.image(
            src="/Imagenes/banner1.png",
            width="100vw",
            height="650px",
            object_fit="cover",
        ),
        width="100%",
        overflow="hidden",
    )