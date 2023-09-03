from flask import Blueprint, request
from app.models.users import User
from app.forms.auth import LoginForm, SignupForm, UpdatePasswordForm


router = Blueprint("auth", __name__, url_prefix="/auth")


@router.route("/signup", methods=["POST"])
def signup():
    form = SignupForm(request.form)
    print("form: ", form.data)
    return "<p>User registered!</p>"

@router.route("/login", methods=["POST"])
def login():    
    form = LoginForm(request.form)
    print("form: ", form.data)
    return "login"

@router.route("/password", methods=["POST"])
def update_password():
    form = UpdatePasswordForm(request.form)
    print("form: ", form.data)
    return "password"