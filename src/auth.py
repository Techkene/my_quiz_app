from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/b1/auth")

@auth.post('/register')
def register():
    return "User created"