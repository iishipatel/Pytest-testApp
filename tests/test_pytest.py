from mock import patch 
from ..src.Services.student_service import *

def test_all_students():
        with patch('testApp.src.Services.student_service.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = [[ 123, "Iishi","Delhi"],[ 234, "Tanya", "Bangalore"]]
            all_students=get_students()
            if len(all_students) == 2:
                assert True

def test_one_students():
        with patch('testApp.src.Services.student_service.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchone.return_value = [ 123, "Iishi","Delhi"]
            one_student= get_by_id(123)
            if len(one_student) == 3:
                assert True






# from ..main import app
# import testApp.Database.db as db
# import requests

# API_URL = "http://0.0.0.0:8000"

# def test_all_students():
#     tester = app.test_client()
#     response = tester.get("{}/students".format(API_URL))
#     statuscode = response.status_code
#     assert statuscode == 200

# def test_1_student():
#     tester = app.test_client()
#     response = tester.get("{}/student/123".format(API_URL))
#     assert response.status_code == 200
#     if b"123" in response.data:
#         assert True

# def test_insert_student(self):
#     tester = app.test_client(self)
#     response = tester.post("/student", json = {"id":234, "name":"Riya", "address":"Bangalore"})
#     statuscode = response.status_code
#     self.assertEqual(statuscode,200)

# def test_update_student(self):
#     tester = app.test_client(self)
#     response = tester.put("/student", json = {"id":234, "name":"Tanya", "address":"Bangalore"})
#     statuscode = response.status_code
#     self.assertEqual(statuscode,200)

# def test_delete_student(self):
#     tester = app.test_client(self)
#     response = tester.delete("/student/234")
#     self.assertEqual(response.status_code,200)
#     self.assertTrue(b"true" in response.data) 

