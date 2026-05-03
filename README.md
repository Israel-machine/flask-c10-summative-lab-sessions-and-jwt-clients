pipenv install
pipenv shell
cd server
export FLASK_APP=app.py
flask shell

#WHAT DOES THIS DO?#
flask db init
flask db migrate
flask db upgrade

#Start Flask Server#:
flask run --port=5555
http://127.0.0.1:5555

#react initializatio#: 
cd client-with-jwt
npm install
npm start

#RUN SEED FILE TO CREATE DUMMY DATA#
Enter the Shell
    flask shell


from models import User
from config import db

# Create the user object
u = User(username="ExampleUser")
u.password_hash = "mypassword"

db.session.add(u)
db.session.commit()



Start Flask Back end:
cd server:
pipenv shell:
python app.py


Start the React Frontend
