from fastapi import FastAPI
from peliculas import obtener_peliculas
from usuarios import registrar_usuario

api = FastAPI()


@api.get("/")
def inicio():
    return {"mensaje": "Sistema de Reservas de Cine"}


@api.get("/peliculas")
def get_peliculas():
    return obtener_peliculas()


@api.post("/registro")
def post_registro(nombre: str, email: str, password: str):
    return registrar_usuario(nombre, email, password)