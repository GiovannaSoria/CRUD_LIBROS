import sqlite3
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


# Clase del servicio
class BookService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, _returns=String)
    def add_book(ctx, title, author, genre):
        connection = sqlite3.connect("database/books.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
        connection.commit()
        connection.close()
        return f"Book '{title}' added successfully."

    @rpc(Integer, _returns=String)
    def delete_book(ctx, book_id):
        connection = sqlite3.connect("database/books.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        connection.close()
        return f"Book with ID {book_id} deleted successfully."

    @rpc(Integer, Unicode, Unicode, Unicode, _returns=String)
    def edit_book(ctx, book_id, title, author, genre):
        connection = sqlite3.connect("database/books.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE books SET title = ?, author = ?, genre = ? WHERE id = ?",
            (title, author, genre, book_id)
        )
        if cursor.rowcount == 0:
            connection.close()
            return f"Book with ID {book_id} not found."
        connection.commit()
        connection.close()
        return f"Book with ID {book_id} updated successfully."

    @rpc(Integer, _returns=Iterable(Unicode))
    def get_book(ctx, book_id):
        connection = sqlite3.connect("database/books.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        connection.close()
        if not book:
            yield f"Book with ID {book_id} not found."
        else:
            yield f"ID: {book[0]}"
            yield f"Title: {book[1]}"
            yield f"Author: {book[2]}"
            yield f"Genre: {book[3]}"

    @rpc(_returns=Iterable(Unicode))
    def list_books(ctx):
        connection = sqlite3.connect("database/books.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        connection.close()
        if not books:
            yield "No books available."
        for book in books:
            yield f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}"


# Configuración de la aplicación SOAP
application = Application(
    [BookService],
    tns="soap.example.bookservice",
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Configuración del servidor WSGI
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Crear base de datos si no existe
    connection = sqlite3.connect("database/books.db")
    cursor = connection.cursor()
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

    # Iniciar el servidor
    wsgi_app = WsgiApplication(application)
    server = make_server("127.0.0.1", 8000, wsgi_app)
    print("SOAP CORRIENDO EN http://127.0.0.1:8000")
    server.serve_forever()
