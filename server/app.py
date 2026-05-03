from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from config import app, db, api
from models import User, Meeting

class Signup(Resource):
    def post(self):
        data = request.get_json()
        try:
            if data['password'] != data['password_confirmation']:
                return {"errors": ["Passwords do not match"]}, 422
                
            user = User(username=data['username'])
            user.password_hash = data['password']
            db.session.add(user)
            db.session.commit()
            
            token = create_access_token(identity=user.id)
            return {"token": token, "user": {"id": user.id, "username": user.username}}, 201
        except Exception as e:
            return {"errors": [str(e)]}, 422

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.authenticate(data.get('password')):
            token = create_access_token(identity=user.id)
            return {"token": token, "user": {"id": user.id, "username": user.username}}, 200
        return {"errors": ["Invalid username or password"]}, 401

class CheckSession(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        return {"id": user.id, "username": user.username}, 200

class MeetingsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        page = request.args.get('page', 1, type=int)
        per_page = 5
        pagination = Meeting.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)
        
        return {
            "meetings": [m.to_dict() for m in pagination.items],
            "total": pagination.total,
            "pages": pagination.pages
        }, 200

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(CheckSession, '/me')
api.add_resource(MeetingsResource, '/meetings')

if __name__ == '__main__':
    app.run(port=5555, debug=True)