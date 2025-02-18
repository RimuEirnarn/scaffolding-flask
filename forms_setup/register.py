"""Register"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class Register(FlaskForm):
    """Register"""

    display_name = StringField("Your display name", [DataRequired()])
    username = StringField("Your username", [DataRequired()])

    password = PasswordField("Password", [DataRequired()])
    retype = PasswordField(
        "Retype your password",
        [DataRequired(), EqualTo("password", "Password must match")],
    )

    submit = SubmitField("Register")
