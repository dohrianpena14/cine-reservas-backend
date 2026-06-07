import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection


def obtener_asientos(funcion_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fila, numero, disponible
        FROM asientos
        WHERE funcion_id = %s
        ORDER BY fila, numero
    """, (funcion_id,))

    asientos = []

    for fila in cursor.fetchall():
        asientos.append({
            "id": fila[0],
            "fila": fila[1],
            "numero": fila[2],
            "disponible": bool(fila[3])
        })

    cursor.close()
    conn.close()

    return asientos