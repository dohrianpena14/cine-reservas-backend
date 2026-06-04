from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT id FROM funciones")
funciones = cursor.fetchall()

filas = ["A", "B", "C", "D", "E"]
numeros = range(1, 11)

for funcion in funciones:
    funcion_id = funcion[0]

    for fila in filas:
        for numero in numeros:
            cursor.execute("""
                INSERT INTO asientos (funcion_id, fila, numero, disponible)
                VALUES (%s, %s, %s, TRUE)
            """, (funcion_id, fila, numero))

conn.commit()
cursor.close()
conn.close()

print("Asientos creados correctamente")