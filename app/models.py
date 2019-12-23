from app import db
from flask_login import UserMixin
from datetime import datetime


class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    sent = db.relationship('Messages', backref='sent', lazy='dynamic', foreign_keys='Messages.sent_by')
    received = db.relationship('Messages', backref='received', lazy='dynamic', foreign_keys='Messages.receive_by')

    def __repr__(self):
        return f'<User: {self.user_id}>'

    def get_id(self):
        return self.user_id


class Messages(UserMixin, db.Model):
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sent_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    receive_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    sender = db.Column(db.String(255))
    receiver = db.Column(db.String(255))
    subject = db.Column(db.String(5000))
    message = db.Column(db.String(500000))
    is_read = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Message: {self.subject}>'

