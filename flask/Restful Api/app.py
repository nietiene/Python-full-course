from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database for study

sutdents = {
    1: {"name": "Etiene", "Age": 17},
    2: {"name": "Alice", "Age": 22},
}

