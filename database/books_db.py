import sqlite3

def initialize_database():
    # Conexión a la base de datos
    connection = sqlite3.connect("database/books.db")
    cursor = connection.cursor()

    # Crear tabla de libros si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()
    print("Base de datos inicializada.")

if __name__ == "__main__":
    initialize_database()
