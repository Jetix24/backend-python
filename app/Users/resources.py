from flask.views import MethodView
from flask import Blueprint, request
from .models import Users

users_blueprint = Blueprint("users_blueprint", __name__,url_prefix='/api/')

class UsersList(MethodView):
    def get(self):
        return [{"name": "Jose"},{"name": "Fer"}]
                
class UsersID(MethodView):
    def get(self, user_id):
        return{"id": user_id, "username": "name"}

class UsersResources(MethodView):
    def post(self):
        print("Hola")
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        rol = data.get('rol')

        if email is None:
            return {"message:" "No has ingresado tu correo."},400
        if username is None:
            return {"message:" "No has ingresado tu username."},400
        
        new_user = Users(username,email,rol)
        new_user.save()

        return "Hola"
        
users_blueprint.add_url_rule(
    'users',
    view_func=UsersList.as_view("users_list")
)

users_blueprint.add_url_rule(
    'users',
    view_func=UsersResources.as_view("users_Resources")
)

users_blueprint.add_url_rule(
    'users/<user_id>',
    view_func=UsersID.as_view("users_id")

)