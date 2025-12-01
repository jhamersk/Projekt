from src.app import create_app
from src.db import db


app = create_app()

with app.app_context():
    print("Applying migrations...")
    db.create_all()
    print("Migrations applied.")
