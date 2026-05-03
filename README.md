ESTUDIOSO: High School Counselor Meeting Tracker App

DESCRIPTION:
    This project demonstrates a robust implementation of Client-Side and Server-Side Authentication.

    Backend: Built with Python and Flask-RESTful, utilizing SQLAlchemy for database management and Flask-JWT-Extended for security.

    Frontend: Built with React, featuring styled-components for UI and a custom JWT-handling system to maintain user sessions.

    Key Features: User signup/login, persistent sessions, and full CRUD (Create, Read, Update, Delete) capabilities for meeting notes.

INSTALLATION
    Required:
        Python 3.8+
        Node.js & npm
        Pipenv

    Set Up Back End:
        cd server
        pipenv install && pipenv shell

    Initialize the database and seed it:
        flask db upgrade
        python seed.py

    Set Up Front End:
        cd client-with-jwt
        npm install

RUN INSTRUCTIONS:
    Run Back End(Flask):
        In your backend terminal (server folder):
            python app.py
            The backend will be accessible at http://localhost:5555.

    Run Front End(React):
        In your frontend terminal (client-with-jwt folder):
            npm start
            The application will open automatically in your browser at http://localhost:4000

In React Front End(Browswer):
    1. You will be able to create an account with a username and password
    2. Login and Logout with that username and password
    3. Add meetings with meeting details: student in question, date of meeting, notes for meeting 
    4. Meetings will be saved and visible to user
    5. User will be able to delete individual meetings 