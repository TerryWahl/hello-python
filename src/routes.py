import os

def set_routes(app):

    port = int(os.getenv("PORT"))

    @app.route('/')
    def hello_world():
        return 'Hello World! I am running on port ' + str(port)
