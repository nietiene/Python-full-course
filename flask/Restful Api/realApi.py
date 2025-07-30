from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# database connection

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='student_api_py',
        cursorclass=pymysql.cursors.DictCursor
    )