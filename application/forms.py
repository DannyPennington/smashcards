from flask_wtf import FlaskForm
from wtforms import StringField, SubmintField, PasswordField, BooleanField
from wtforms.validators import Length, Email, DataRequired, EqualTo, ValidationError
from application.models import Users

class RegistrationForm(FlaskForm):
    forename = StringField("First name",
            validators = [
                DataRequired(),
                Length(min=1,max=30)
                ]
            )
    surname = StringField("Last name",
            validators = [
                DataRequired(),
                Length(min=1,max=50)
                ]
            )
    username = StringField("Username",
            validators = [
                DataRequired(),
                Length(min=1,max=50)
                ]
            )
    email = StringField("Email",
            validators = [
                DataRequired(),
                Length(min=1,max=50),
                Email()
                ]
            )
    password = PasswordField("Password",
            validators = [
                DataRequired(),
                Length(min=1,max=30)
                ]
            )
    confirm_password = PasswordField("Confirm Password",
            validators = [
                DataRequired(),
                Length(min=1,max=50),
                EqualTo("password")
                ]
            )
    submit = SubmitField("Sign up!")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already registered, please sign in instead")
