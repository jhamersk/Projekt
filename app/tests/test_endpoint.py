import pytest
from src.db import db
from src.models import User, Task, Product
from src.app import create_app


@pytest.fixture
def app():
    test_config = {"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", "TESTING": True}
    app = create_app(test_config)

    with app.app_context():
        db.create_all()
        user1 = User(name="Ola")
        user2 = User(name="Ania")
        db.session.add_all([user1, user2])
        db.session.commit()

        task1 = Task(title="Task 1", completed=False, user_id=user1.id)
        task2 = Task(title="Task 2", completed=True, user_id=user1.id)
        db.session.add_all([task1, task2])
        db.session.commit()

        product1 = Product(name="Product 1", price=10.5)
        product2 = Product(name="Product 2", price=20.0)
        db.session.add_all([product1, product2])
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json == {"status": "ok"}


def test_get_users(client):
    res = client.get("/users")
    assert res.status_code == 200
    assert len(res.json) == 2
    assert res.json[0]["name"] in ["Ola", "Ania"]
    assert "tasks" in res.json[0]


def test_get_tasks(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    assert len(res.json) == 2
    assert "title" in res.json[0]
    assert "completed" in res.json[0]
    assert "user_id" in res.json[0]


def test_get_products(client):
    res = client.get("/products")
    assert res.status_code == 200
    assert len(res.json) == 2
    assert "name" in res.json[0]
    assert "price" in res.json[0]
