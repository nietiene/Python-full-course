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

# Get all students in database
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)


# get one student by ID
app.route('/students/<int:student_id', methods=['GET'])
def get_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    row = cursor.fetchall()
    conn.close()