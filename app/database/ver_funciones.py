from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM funciones")

funciones = cursor.fetchall()

for funcion in funciones:
    print(funcion)

cursor.close()
conn.close()