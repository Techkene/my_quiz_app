from flask_sqlalchemy import SQLAlchemy
from enum import unique
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

db = SQLAlchemy()

class User(db.Model):
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

