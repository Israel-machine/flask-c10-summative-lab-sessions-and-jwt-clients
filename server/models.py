#CREATES COLUMNS FOR USERS & MEETING TABLES
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import db, bcrypt

#. models.py (The Skeleton)
# Action: Define your User and Meeting classes. Add the password hashing logic and relationships.
# Why: Everything in your app depends on the shape of your data. You can't have a login route if you don't have a User model.

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_Key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    meetings = db.relationship('Meeting', back_populates='user', cascade='all, delete-orphan')


    @validates('username')
    def validate_username(self, key, username):
        if not username or len(username) < 3:
            raise ValueError("Username must be 3 or more characters long.")
        return username
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        pw_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = pw_hash.decode('utf-8')
    
    
class Meeting(db.Model):