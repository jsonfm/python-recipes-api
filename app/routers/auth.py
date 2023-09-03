from flask import Blueprint, request, jsonify
from app.models.users import User
from app.forms.auth import LoginForm, SignupForm, UpdatePasswordForm
from app.utils.auth import apply_hash_password
from app.utils.encrypt import check_password


router = Blueprint("auth", __name__, url_prefix="/auth")


@router.route("/signup", methods=["POST"])
def signup():
    form = SignupForm(request.form)
    if form.validate():
        form = apply_hash_password(form)
        user = User(username=form.email.data, email=form.email.data, password=form.password.data)
        user.save()
        user = user.to_dict()
        return jsonify(user)
    response = jsonify({"errors": form.errors})
    return response, 400


@router.route("/login", methods=["POST"])
def login():    
    form = LoginForm(request.form)
    if form.validate():
        user = User.get_by_email(form.email.data, to_dict=False)
        if user is not None:
            if check_password(form.password.data, user.password):
                return "password"
    return "Invalid email or password.", 403


@router.route("/password", methods=["POST"])
def update_password():
    form = UpdatePasswordForm(request.form)
    return "password"