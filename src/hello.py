from flask import Flask
import os
from routes import set_routes

port = int(os.getenv("PORT"))
app = Flask(__name__)

set_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
