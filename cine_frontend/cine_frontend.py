import reflex as rx

from cine_frontend.pages.home import home
from cine_frontend.pages.cartelera import cartelera

app = rx.App()

app.add_page(home, route="/")
app.add_page(cartelera, route="/cartelera")