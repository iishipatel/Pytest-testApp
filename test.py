import unittest
from mock import patch 
from Controllers.student_controller import *
from flask import jsonify

class APITest(unittest.TestCase):


    def test_all_students(self):
        with patch('Controllers.student_controller.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = [[ 123, "Iishi","Delhi"],[ 234, "Tanya", "Bangalore"]]
            all_students=get_students()
            self.assertEqual(len(all_students),2)

    def test_one_students(self):
        with patch('Controllers.student_controller.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchone.return_value = [ 123, "Iishi","Delhi"]
            one_student= get_by_id(123)
            self.assertEqual(len(one_student),3)

    # def test_1_student(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/student/123")
    #     self.assertEqual(response.status_code,200)
    #     self.assertTrue(b"123" in response.data)

    # def test_insert_student(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/student", json = {"id":234, "name":"Riya", "address":"Bangalore"})
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)
    #     self.assertTrue(b"true" in response.data)

    # def test_update_student(self):
    #     tester = app.test_client(self)
    #     response = tester.put("/student", json = {"id":234, "name":"Tanya", "address":"Bangalore"})
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)
    #     self.assertTrue(b"true" in response.data)
    
    # def test_delete_student(self):
    #     tester = app.test_client(self)
    #     response = tester.delete("/student/234")
    #     self.assertEqual(response.status_code,200)
    #     self.assertTrue(b"true" in response.data) 

if __name__ == "__main__":
    unittest.main()