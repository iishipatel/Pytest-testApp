from __main__ import app
import src.Services.student_service as SC
from flask import jsonify, request

@app.route('/students', methods=["GET"])
def get_students():
    students = SC.get_students()
    return jsonify(students)


@app.route("/student", methods=["POST"])
def insert_student():
    student_details = request.get_json()
    id = student_details["id"]
    name = student_details["name"]
    address = student_details["address"]
    result = SC.insert_student(id, name, address)
    return jsonify(result)

@app.route("/student", methods=["PUT"])
def update_student():
    student_details = request.get_json()
    id = student_details["id"]
    name = student_details["name"]
    address = student_details["address"]
    result = SC.update_student(id, name, address)
    return jsonify(result)


@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    result = SC.delete_student(id)
    return jsonify(result)


@app.route("/student/<id>", methods=["GET"])
def get_student_by_id(id):
    student = SC.get_by_id(id)
    return jsonify(student)
