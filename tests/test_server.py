import pytest
from zeep import Client

# URL del servidor
WSDL_URL = "http://127.0.0.1:8000/?wsdl"

@pytest.fixture
def client():
    return Client(wsdl=WSDL_URL)

def test_add_book(client):
    response = client.service.add_book("1984", "George Orwell", "Dystopian")
    assert "added successfully" in response

def test_list_books(client):
    response = client.service.list_books()
    assert isinstance(response, list)  # Verifica que se retorna una lista

def test_get_book(client):
    response = client.service.get_book(1)
    assert "Title:" in response[0]  # Verifica que el libro tiene título

def test_delete_book(client):
    response = client.service.delete_book(2)
    assert "deleted successfully" in response
