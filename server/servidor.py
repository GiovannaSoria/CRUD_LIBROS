from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from services import BookService

# Configuración de la aplicación SOAP
application = Application(
    [BookService],
    tns="soap.example.bookservice",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print("Servidor SOAP corriendo en http://127.0.0.1:8000")
    server = make_server("127.0.0.1", 8000, WsgiApplication(application))
    server.serve_forever()
