import os #access environment variables (like secret keys or database URLs) for security.
from flask import Flask #initializes web application instance,
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__) #creates main application object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counselor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default-dev-key')

db = SQLAlchemy()
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)

db.init_app(app)
