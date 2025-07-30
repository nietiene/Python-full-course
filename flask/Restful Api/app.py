from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# fake database for study

sutdents = {
    1: {"name": "Etiene", "Age": 17},
    2: {"name": "Alice", "Age": 22},

}