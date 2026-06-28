from database.db import *
from models.courses import courses

#add course
def add_course():
    conn= get_connection()
    cursor= conn.cursor()

    course_name = input("Enter course name:")
    course