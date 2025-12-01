import os
import csv
import json

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

    print("Writing output files")

    os.makedirs("/seed_output", exist_ok=True)

    with open("/seed_output/users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
        for u in users:
            writer.writerow([u.id, u.name])

    with open("/seed_output/tasks.json", "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)

    with open("/seed_output/products.json", "w") as f:
        json.dump([p.to_dict() for p in products], f, indent=2)

    with open("/seed_output/seed.log", "w") as f:
        f.write("Seed completed successfully.\n")

    print("Seeder finished.")
