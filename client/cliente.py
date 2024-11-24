from zeep import Client

# URL del WSDL
wsdl = "http://127.0.0.1:8000/?wsdl"
client = Client(wsdl=wsdl)

# Agregar un libro
print("=== Agregar un libro ===")
add_response = client.service.add_book("Revelion de atlas", "Ayn Rand", "Novela Filosofica")
print(add_response)

# Listar libros para verificar que se agregó
print("\n=== Listar libros ===")
list_response = client.service.list_books()
if list_response:
    for book in list_response:
        print(book)
else:
    print("No hay libros disponibles.")

# Editar el libro
print("\n=== Editar el libro ===")
edit_response = client.service.edit_book(11, "El hombre mas rico de babilonia", "George Clasom", "Finanzas")
print(edit_response)

# Listar libros nuevamente para verificar los cambios
print("\n=== Listar libros después de la edición ===")
list_response = client.service.list_books()
if list_response:
    for book in list_response:
        print(book)
else:
    print("No hay libros disponibles.")

# Borrar el libro
print("\n=== Eliminar el libro ===")
delete_response = client.service.delete_book(12)
print(delete_response)

# Listar libros nuevamente para verificar que se eliminó
print("\n=== Listar libros después de la eliminación ===")
list_response = client.service.list_books()
if list_response:
    for book in list_response:
        print(book)
else:
    print("No hay libros disponibles.")
