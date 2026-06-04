from fastapi import FastAPI
from peliculas import obtener_peliculas

api = FastAPI()


@api.get("/")
def inicio():
    return {
        "mensaje": "Sistema de Reservas de Cine"
    }


@api.get("/peliculas")
def get_peliculas():
    return obtener_peliculas()