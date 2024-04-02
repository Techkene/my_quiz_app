from flask_sqlalchemy import SQLAlchemy
from enum import unique
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.column(db.Interger, primary_key=True)
    username = db.column(db.Strings(80), unique=True, nullable=False)
    email = db.column(db.Strings(80), unique=True, nullable=False)
    password = db.column(db.Text(120), nullable=False)
    created_at = db.column(db.DateTime, default=datetime.now())
    updated_at = db.column(db.DateTime, onupdate=datetime.now())
    questions = db.relationship("Question", backref="creator")
    is_admin = db.Column(db.Boolean, default=False)
    result = db.relationship("Result", backref="user")

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __repr__(self):
        return f"User({self.id}, '{self.name}')"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, unique=False, nullable=False)
    option1 = db.Column(db.String, nullable=False)
    option2 = db.Column(db.String, nullable=False)
    option3 = db.Column(db.String, nullable=False)
    option4 = db.Column(db.String, nullable=False)
    correct_option = db.Column(db.CHAR, nullable=False)
    verified = db.Column(db.Boolean, nullable=False, default=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    question_set_id = db.Column(db.Integer, db.ForeignKey("questionset.id"), nullable=True)

    def __repr__(self):
        return f"Question({self.id}, '{self.question}', {self.creator})"