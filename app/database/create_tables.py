from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Películas
cursor.execute("""
CREATE TABLE IF NOT EXISTS peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    genero VARCHAR(50),
    duracion INT,
    clasificacion VARCHAR(20),
    precio DECIMAL(10,2) NOT NULL,
    imagen_url VARCHAR(255),
    activa BOOLEAN DEFAULT TRUE
)
""")

# Funciones
cursor.execute("""
CREATE TABLE IF NOT EXISTS funciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pelicula_id INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    sala VARCHAR(20) NOT NULL,
    FOREIGN KEY (pelicula_id) REFERENCES peliculas(id)
)
""")

# Asientos
cursor.execute("""
CREATE TABLE IF NOT EXISTS asientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    funcion_id INT NOT NULL,
    fila VARCHAR(5) NOT NULL,
    numero INT NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (funcion_id) REFERENCES funciones(id)
)
""")

# Reservas
cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    funcion_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (funcion_id) REFERENCES funciones(id)
)
""")

# Detalle de asientos reservados
cursor.execute("""
CREATE TABLE IF NOT EXISTS reserva_asientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reserva_id INT NOT NULL,
    asiento_id INT NOT NULL,
    FOREIGN KEY (reserva_id) REFERENCES reservas(id),
    FOREIGN KEY (asiento_id) REFERENCES asientos(id)
)
""")

conn.commit()
cursor.close()
conn.close()

print("Tablas creadas correctamente")