from zeep import Client

def test_list_books():
    wsdl = "http://127.0.0.1:8000/?wsdl"
    client = Client(wsdl=wsdl)
    response = client.service.list_books()
    assert isinstance(response, list)
