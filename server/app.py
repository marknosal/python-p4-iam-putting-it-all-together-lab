#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe

class Signup(Resource):
    def post(self):
        json = request.get_json()
        
        new_user = User(
            username = json['username'],
            image_url = ['image_url'],
            bio = json['bio']
        )
        new_user.password_hash = json.get('password')

        try:
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id

            return new_user.to_dict(), 201
        
        except IntegrityError:
            return {'error': '422 Cannot process'}, 422

class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass

class RecipeIndex(Resource):
    pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
