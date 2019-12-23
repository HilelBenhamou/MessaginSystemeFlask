from app import app, db, login_manager
from app.models import Users, Messages
from app.forms import Register, Login, WriteMessage
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def registration():
    register = Register()
    login = Login()

    if register.validate_on_submit():
        name = register.name.data
        lastname = register.lastname.data
        email = register.email.data
        username = register.username.data
        password = register.password.data

        newUser = Users(name=name, lastname=lastname, email=email, username=username, password=password)
        db.session.add(newUser)
        db.session.commit()
        flash('You are successfully registred!', 'success')
        return redirect('/')

    elif login.validate_on_submit():
        email = login.email.data
        password = login.password.data

        user = Users.query.filter_by(email=email).first()
        user_password = Users.query.filter_by(password=password).first()

        if user:
            if user_password:
                login_user(user)
            else:
                return '<h1>Invalid password</h1>'
        else:
            return '<h1>Invalid email or password</h1>'

        return redirect('/dashboard')

    return render_template('login_register.html', register=register, login=login)


@app.route('/dashboard/', defaults={'is_read': None, 'message_id': None}, methods=['GET', 'POST'])
@app.route('/dashboard/<is_read>/<int:message_id>', methods=['GET', 'POST'])
@login_required
def dashboard(is_read, message_id):
    current_name = current_user.name
    current_email = current_user.email
    current_sent = current_user.sent
    current_received = current_user.received
    confirm = 'Your mail is sent !'

    write = WriteMessage()
    # If form email sent
    if write.validate_on_submit():
        sent_by = write.sender.data
        receive_by = write.receiver.data
        subject = write.subject.data
        message = write.message.data

        if sent_by.lower() not in [user.email.lower() for user in Users.query.all()]:
            return 'The sender is not in the database'
        else:
            sent = Users.query.filter_by(email=sent_by).first()
            if receive_by.lower() not in [user.email.lower() for user in Users.query.all()]:
                return 'The receiver is not in the database'
            else:
                received = Users.query.filter_by(email=receive_by).first()

        newMessage = Messages(sent=sent, received=received, sender=sent_by, receiver=receive_by, subject=subject,
                              message=message, creation_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(newMessage)
        db.session.commit()

        return render_template('dashboard.html', write=write, confirm=confirm, current_name=current_name,
                               current_sent=current_sent, current_received=current_received,
                               current_email=current_email)
    # If form email NOT sent

    if is_read:
        for info in current_sent:
            if info.message_id == message_id:
                all_infos = info
                return render_template('conversations.html', write=write, current_name=current_name,
                                       current_sent=current_sent,
                                       current_received=current_received, current_email=current_email,
                                       all_infos=all_infos, all_infos_received=all_infos)
        for info in current_received:
            if info.message_id == message_id:
                all_infos = info
                return render_template('conversations.html', write=write, current_name=current_name,
                                       current_sent=current_sent,
                                       current_received=current_received, current_email=current_email,
                                       all_infos_received=all_infos, all_infos=all_infos)

    else:
        return render_template('dashboard.html', write=write, current_name=current_name, current_sent=current_sent,
                               current_received=current_received, current_email=current_email)


# @login_required
# def conversation():
#     current_sent = current_user.sent
#     current_received = current_user.received
#     return render_template('conversations.html', current_received=current_received, current_sent=current_sent)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
