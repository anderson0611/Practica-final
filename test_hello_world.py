import pytest
import requests
from pytest_httpserver import HTTPServer

@pytest.fixture
def httpserver():
    server = HTTPServer()
    server.start()  # Asegúrate de que el servidor esté en ejecución
    yield server
    if server.is_running():
        server.stop()

def test_hello_world(httpserver):
    # Lee el contenido del archivo
    with open('index.html', 'r') as file:
        content = file.read()

    # Configura la respuesta del servidor
    httpserver.expect_request('/').respond_with_data(content)

    # Aquí puedes hacer la solicitud y verificar la respuesta
    response = requests.get(f'http://localhost:{httpserver.port}/')
    assert response.text == content