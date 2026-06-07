# app/database/ver_peliculas.py

from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT id, titulo, genero, precio FROM peliculas")

for pelicula in cursor.fetchall():
    print(pelicula)

cursor.close()
conn.close()