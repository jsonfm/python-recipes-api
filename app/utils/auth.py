from app.utils.encrypt import hash_password
from app.forms.auth import LoginForm


def apply_hash_password(form: LoginForm):
    data = form.data
    data = {
        **data,
        "password": hash_password(form.password.data)
    }
    new_form = LoginForm(**data)
    return new_form