from flask import Flask
import os
from src.routes import set_routes

class TestHello:

    def test_math(self):
        assert 3 + 2 == 5

    def test_hello(self):
        # ARRANGE
        port = int(os.getenv("PORT"))
        app = Flask(__name__)
        client = app.test_client()
        set_routes(app)

        # ACT
        url = '/'
        response = client.get(url)

        # ASSERT
        assert not b'Beep' in response.get_data()
        assert response.get_data() == b'Hello World! I am running on port ' + str(port)
        assert response.status_code == 200
