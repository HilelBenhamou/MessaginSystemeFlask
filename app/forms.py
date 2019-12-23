from flask_wtf import FlaskForm
from wtforms.validators import data_required, Email
from wtforms import StringField, SubmitField, PasswordField, TextAreaField


class Register(FlaskForm):
    name = StringField('Name :', validators=[data_required()])
    lastname = StringField('Lastname :', validators=[data_required()])
    email = StringField('Email :', validators=[data_required(), Email()])
    username = StringField('Username :', validators=[data_required()])
    password = PasswordField('Password :', validators=[data_required()])
    submit = SubmitField('Register')


class Login(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Login')


class WriteMessage(FlaskForm):
    sender = StringField('From :', validators=[data_required()])
    receiver = StringField('To :', validators=[data_required()])
    subject = StringField('Subject :', validators=[data_required()])
    message = TextAreaField('Message :', validators=[data_required()])
    submit = SubmitField('Send')





# <!--{% block mess_block %}-->
# <!--    {% for info in current_sent %}-->
# <!--        <p style="border:1px solid navy;">{{ info.message }}</p>-->
# <!--    {% endfor %}-->
# <!--{% endblock %}-->