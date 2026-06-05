import reflex as rx

config = rx.Config(
    app_name="cine_frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)