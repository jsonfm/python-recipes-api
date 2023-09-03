from wtforms import Form, BooleanField, StringField, PasswordField, validators


class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])


class SignupForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    confirm = PasswordField('Confirm', [
        validators.DataRequired(),
    ])

class UpdatePasswordForm(Form):
    password = PasswordField('Password')
    confirm = PasswordField('Confirm')