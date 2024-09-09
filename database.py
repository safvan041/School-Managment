from pymongo import MongoClient

def connect_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.school
    return db

db = connect_db()
students = db.students
attendance = db.attendance
grades = db.grades
