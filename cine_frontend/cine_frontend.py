import reflex as rx

from cine_frontend.pages.home import home
from cine_frontend.pages.proximamente import proximamente
from cine_frontend.pages.eventos import eventos
from cine_frontend.pages.login import login
from cine_frontend.pages.registrar import registrar
from cine_frontend.pages.pelicula import pelicula
from cine_frontend.pages.reserva import reserva


app = rx.App()


app.add_page(home, route="/")
app.add_page(proximamente, route="/proximamente")
app.add_page(eventos, route="/eventos")
app.add_page(login, route="/login")
app.add_page(registrar, route="/registrar")

# Nuevas páginas
app.add_page(pelicula, route="/pelicula")
app.add_page(reserva, route="/reserva")