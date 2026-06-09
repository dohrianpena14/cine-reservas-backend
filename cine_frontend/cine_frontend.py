import reflex as rx

from cine_frontend.pages.home import home
from cine_frontend.pages.proximamente import proximamente
from cine_frontend.pages.eventos import eventos

app = rx.App()

app.add_page(home, route="/")
app.add_page(proximamente, route="/proximamente")
app.add_page(eventos, route="/eventos")