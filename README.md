pipenv install
pipenv shell
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
npm install
npm start

#RUN SEED FILE TO CREATE DUMMY DATA#