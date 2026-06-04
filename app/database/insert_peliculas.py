from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO peliculas
(titulo, descripcion, genero, duracion, clasificacion, precio, imagen_url)
VALUES
(
    'Avengers Endgame',
    'Los Vengadores enfrentan a Thanos.',
    'Accion',
    181,
    'PG-13',
    10.00,
    'endgame.jpg'
),
(
    'Spider-Man No Way Home',
    'Peter Parker abre el multiverso.',
    'Accion',
    148,
    'PG-13',
    12.00,
    'spiderman.jpg'
),
(
    'Inside Out 2',
    'Las emociones regresan.',
    'Animacion',
    96,
    'PG',
    8.00,
    'insideout2.jpg'
)
""")

conn.commit()
cursor.close()
conn.close()

print("Peliculas insertadas correctamente")