from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint

class HelloWorld(MethodView):
    def get(self):
        return {'message': 'het there Hello world :)'}
    

def create_app():
    app = Flask(__name__)

    hello_world = HelloWorld.as_view("hello_world")

    app.add_url_rule('/', view_func=hello_world)
    app.add_url_rule('/api/', view_func=hello_world)
    app.add_url_rule('/new_url/', view_func=hello_world)
    app.register_blueprint(users_blueprint)

    return app