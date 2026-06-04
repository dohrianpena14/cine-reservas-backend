from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO funciones (pelicula_id, fecha, hora, sala)
VALUES
(1, '2026-06-05', '18:00:00', 'Sala 1'),
(1, '2026-06-05', '21:00:00', 'Sala 1'),
(2, '2026-06-06', '19:00:00', 'Sala 2'),
(3, '2026-06-06', '17:00:00', 'Sala 3')
""")

conn.commit()

cursor.close()
conn.close()

print("Funciones insertadas correctamente")