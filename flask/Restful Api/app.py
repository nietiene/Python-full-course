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
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student)
    return jsonify({ "message": "Student not found" }), 404

# POST- add new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_id = max(students.keys()) + 1
    students[new_id] = data
    return jsonify({ "message": "Student added", "id": new_id, "student": data}), 201


if __name__ == "__main__":
    app.run(debug=True)