from fastapi import FastAPI

from peliculas import obtener_peliculas
from usuarios import registrar_usuario, login_usuario
from funciones import obtener_funciones

api = FastAPI(
    title="Sistema de Reservas de Cine",
    version="1.0.0"
)


@api.get("/")
def inicio():
    return {
        "mensaje": "Sistema de Reservas de Cine"
    }


@api.get("/peliculas")
def get_peliculas():
    return obtener_peliculas()


@api.post("/registro")
def post_registro(
    nombre: str,
    email: str,
    password: str
):
    return registrar_usuario(
        nombre,
        email,
        password
    )


@api.post("/login")
def post_login(
    email: str,
    password: str
):
    return login_usuario(
        email,
        password
    )


@api.get("/funciones")
def get_funciones():
    return obtener_funciones()