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
    if row:
        return jsonify(row)
    return jsonify({ "message": "Student not found" }), 404


# POST - create a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    age = data['age']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES(%s, %s)", (name, age))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return jsonify({ "id": student_id , "name": name, "age": age}), 201


# PUT - update student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s WHERE id = %s", (name, age, student_id))
    conn.commit()
    conn.close()
    return jsonify({ "messatge": "Student updated" })   

if __name__ == "__main__":
    app.run(debug=True)