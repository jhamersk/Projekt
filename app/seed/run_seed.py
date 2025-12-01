from src.app import create_app
from src.db import db
from src.models import User, Task, Product

app = create_app()

with app.app_context():
    print("Seeding database...")

    users = [
        User(name="Jan"),
        User(name="Adam"),
    ]

    for u in users:
        db.session.add(u)
    db.session.commit()

    tasks = [
        Task(title="Flask Application", user_id=users[0].id, completed=True),
        Task(title="Docker Setup", user_id=users[1].id),
        Task(title="Database Seeder", user_id=users[1].id),
        Task(title="NGINX", user_id=users[0].id),
        Task(title="Testing & CI", user_id=users[0].id),
        Task(title="Azure IaC", user_id=users[1].id),
    ]

    for t in tasks:
        db.session.add(t)

    products = [
        Product(name="Laptop", price=3500.00),
        Product(name="Komputer", price=5000.0),
    ]

    for p in products:
        db.session.add(p)

    db.session.commit()

    print("Seeder finished.")
