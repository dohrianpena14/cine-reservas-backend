from fastapi import FastAPI

from app.api.peliculas import obtener_peliculas
from app.api.usuarios import registrar_usuario, login_usuario
from app.api.funciones import obtener_funciones
from app.api.asientos import obtener_asientos
from app.api.reservas import crear_reserva

api = FastAPI(
    title="Sistema de Reservas de Cine",
    version="1.0.0"
)


@api.get("/")
def inicio():
    return {"mensaje": "Sistema de Reservas de Cine"}


@api.get("/peliculas")
def get_peliculas():
    return obtener_peliculas()


@api.post("/registro")
def post_registro(nombre: str, email: str, password: str):
    return registrar_usuario(nombre, email, password)


@api.post("/login")
def post_login(email: str, password: str):
    return login_usuario(email, password)


@api.get("/funciones")
def get_funciones():
    return obtener_funciones()


@api.get("/asientos/{funcion_id}")
def get_asientos(funcion_id: int):
    return obtener_asientos(funcion_id)


@api.post("/reservas")
def post_reserva(usuario_id: int, funcion_id: int, asiento_id: int):
    return crear_reserva(usuario_id, funcion_id, asiento_id)