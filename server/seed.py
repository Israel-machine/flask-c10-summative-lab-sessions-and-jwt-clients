from faker import Faker
from config import app, db
from models import User, Meeting
import random

fake = Faker()

def run_seed():
    with app.app_context():
        print("Emptying database...")
        User.query.delete()
        Meeting.query.delete()

        print("Creating users (Counselors)...")
        users = []
        for i in range(5):
            user = User(
                username=fake.user_name()
            )
            user.password_hash = "password123" 
            users.append(user)
            db.session.add(user)

        db.session.commit()

        print("Creating student meetings...")
        for _ in range(25):
            meeting = Meeting(
                student_name=fake.name(),
                meeting_date=fake.date_this_year().strftime("%Y-%m-%d"),
                notes=fake.paragraph(nb_sentences=3),
                user=random.choice(users)
            )
            db.session.add(meeting)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    run_seed()