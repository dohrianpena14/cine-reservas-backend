import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.database.connection import get_connection


def registrar_usuario(nombre, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    if usuario:
        cursor.close()
        conn.close()
        return {"mensaje": "El email ya está registrado"}

    cursor.execute("""
        INSERT INTO usuarios (nombre, email, password)
        VALUES (%s, %s, %s)
    """, (nombre, email, password))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensaje": "Usuario registrado correctamente"}