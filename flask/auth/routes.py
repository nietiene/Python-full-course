from flask import Blueprint

# create blueprint
auth = Blueprint('auth', __name__)

# define routes
@auth.route('/login')
def login():
    return "<h2>Login page</h2>"

@auth.route('/register')
def register():
    return "<h2>Register Page</h2>"
