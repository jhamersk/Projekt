from flask import Blueprint, jsonify
from src.models import User, Task, Product

bp = Blueprint("api", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@bp.get("/users")
def get_users():
    return jsonify([u.to_dict() for u in User.query.all()])


@bp.get("/tasks")
def get_tasks():
    return jsonify([t.to_dict() for t in Task.query.all()])


@bp.get("/products")
def get_products():
    return jsonify([p.to_dict() for p in Product.query.all()])
