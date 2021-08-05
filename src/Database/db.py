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

def drop_all():
    db = get_db()
    cursor = db.cursor()
    query = """DROP TABLE students"""
    cursor.execute(query)
