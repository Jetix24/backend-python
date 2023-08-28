from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint
from .Categories.resources import categories_blueprint
from .Roles.resources import roles_blueprint
from .Database import db
from flask_migrate import Migrate

class HelloWorld(MethodView):
    def get(self): # Methods: Create:post Read: get Update: put/path Delete: delete 
        return {'message': 'het there Hello world :)'}
    
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../settings.py')

    db.init_app(app)

    with app.app_context():
        migrate.init_app(app, db)


    hello_world = HelloWorld.as_view("hello_world")
    app.add_url_rule('/', view_func=hello_world) # definir rutas que se encuentran en el proyecto 
    app.add_url_rule('/api/', view_func=hello_world)
    # app.add_url_rule('/new_url/', view_func=hello_world)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(roles_blueprint)
    

    return app