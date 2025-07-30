from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database for study

students = {
    1: {"name": "Etiene", "Age": 17},
    2: {"name": "Alice", "Age": 22},
}


# get all studentd
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# get one student by ID
@app.route('/students/<int:student_id', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student)
    return jsonify({ "message": "Student not found" }), 404

# POST- add new student