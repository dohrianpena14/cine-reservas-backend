import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from app.database.connection import get_connection


def obtener_peliculas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            titulo,
            descripcion,
            genero,
            duracion,
            clasificacion,
            precio,
            imagen_url
        FROM peliculas
        WHERE activa = TRUE
    """)

    filas = cursor.fetchall()

    peliculas = []

    for fila in filas:
        peliculas.append({
            "id": fila[0],
            "titulo": fila[1],
            "descripcion": fila[2],
            "genero": fila[3],
            "duracion": fila[4],
            "clasificacion": fila[5],
            "precio": float(fila[6]),
            "imagen_url": fila[7]
        })

    cursor.close()
    conn.close()

    return peliculas