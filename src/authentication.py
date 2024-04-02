from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.post('/register')
def register():
    return "User created"

@auth.get("/me")
def me():
    return {"user": "me"}