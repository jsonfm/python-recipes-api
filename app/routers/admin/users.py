from flask import Blueprint, request
from app.models.users import User


router = Blueprint("users", __name__)


@router.route("/users")
def users():
    users = User.query.limit(10).all()
    return "users"

@router.route("/users/<int:user_id>")
def user(user_id):
    user = User.query.filter(User.id == user_id).first()
    print("user: ", user)
    return "user"