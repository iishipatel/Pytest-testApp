# from Database.db import get_db
import sqlite3
DATABASE_NAME = "student.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
				address TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def get_students():
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT * FROM students"
    cursor.execute(statement)
    return cursor.fetchall()

def get_by_id(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT id, name, address FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def insert_student(id, name, add):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "INSERT INTO students(id, name, address) VALUES (?, ?, ?)"
    cursor.execute(statement, [id, name, add])
    db.commit()
    return True


def update_student(id, name, add):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "UPDATE students SET name = ?, address = ? WHERE id = ?"
    cursor.execute(statement, [name, add, id])
    db.commit()
    return True


def delete_student(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "DELETE FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


