import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from app.database.connection import get_connection


def obtener_funciones():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            f.id,
            p.titulo,
            f.fecha,
            f.hora,
            f.sala
        FROM funciones f
        INNER JOIN peliculas p
        ON f.pelicula_id = p.id
        ORDER BY f.fecha, f.hora
    """)

    funciones = []

    for fila in cursor.fetchall():
        funciones.append({
            "id": fila[0],
            "pelicula": fila[1],
            "fecha": str(fila[2]),
            "hora": str(fila[3]),
            "sala": fila[4]
        })

    cursor.close()
    conn.close()

    return funciones