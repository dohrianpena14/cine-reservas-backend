import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from app.database.connection import get_connection


def crear_reserva(usuario_id: int, funcion_id: int, asiento_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT disponible
        FROM asientos
        WHERE id = %s AND funcion_id = %s
    """, (asiento_id, funcion_id))

    asiento = cursor.fetchone()

    if not asiento:
        cursor.close()
        conn.close()
        return {"error": "Asiento no encontrado para esa función"}

    if not asiento[0]:
        cursor.close()
        conn.close()
        return {"error": "Ese asiento ya está ocupado"}

    # Crear la reserva
    cursor.execute("""
        INSERT INTO reservas (usuario_id, funcion_id, total)
        VALUES (%s, %s, %s)
    """, (usuario_id, funcion_id, 0))

    reserva_id = cursor.lastrowid

    # Relacionar asiento con la reserva
    cursor.execute("""
        INSERT INTO reserva_asientos (reserva_id, asiento_id)
        VALUES (%s, %s)
    """, (reserva_id, asiento_id))

    # Marcar asiento como ocupado
    cursor.execute("""
        UPDATE asientos
        SET disponible = FALSE
        WHERE id = %s
    """, (asiento_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Reserva creada correctamente"}