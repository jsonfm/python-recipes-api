from flask import Blueprint, request
from app.models.users import User


router = Blueprint("auth", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    user = User(username="franciscomacas3@gmail.com", email="franciscomacas3@gmail.com", password="password")
    user.save()
    return "<p>User registered!</p>"

@router.route("/login", methods=["POST"])
def login():
    form = request.form
    print("form: ", form)
