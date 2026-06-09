import reflex as rx


def carousel():
    return rx.box(
        rx.el.style("""
            @keyframes fade1 {
                0%, 30% { opacity: 1; }
                33%, 100% { opacity: 0; }
            }

            @keyframes fade2 {
                0%, 30% { opacity: 0; }
                33%, 63% { opacity: 1; }
                66%, 100% { opacity: 0; }
            }

            @keyframes fade3 {
                0%, 63% { opacity: 0; }
                66%, 96% { opacity: 1; }
                100% { opacity: 0; }
            }
        """),

        rx.image(
            src="/Imagenes/banner1.png",
            width="100%",
            height="500px",
            object_fit="contain",
            object_position="center",
            position="absolute",
            top="0",
            left="0",
            animation="fade1 12s infinite",
        ),

        rx.image(
            src="/Imagenes/banner2.png",
            width="100%",
            height="500px",
            object_fit="contain",
            object_position="center",
            position="absolute",
            top="0",
            left="0",
            animation="fade2 12s infinite",
        ),

        rx.image(
            src="/Imagenes/banner3.png",
            width="100%",
            height="500px",
            object_fit="contain",
            object_position="center",
            position="absolute",
            top="0",
            left="0",
            animation="fade3 12s infinite",
        ),

        position="relative",
        width="100%",
        height="500px",

        # mismo color del home/navbar para los laterales
        bg="linear-gradient(90deg, #08152f 0%, #0b1d42 50%, #08152f 100%)",

        overflow="hidden",
        margin_top="30px",
        margin_bottom="20px",

        # mismo estilo que se ve en tu captura
        border_radius="16px",
        box_shadow="0 8px 25px rgba(0,0,0,0.35)",
    )