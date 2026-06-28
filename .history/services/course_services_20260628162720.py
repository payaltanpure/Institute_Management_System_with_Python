from database.db import *
from models.courses import courses

#add course
def add_course():
    conn= get_connection()
    cursor= conn.cursor()

    course_name = input("Enter course name:")
    duration= int(input("Enter duration:"))
    fees= float(input("Enter fees"))

    c= courses(course_name,duration, fees)

    query= ("insert into courses(course_name, duration, fees) values(%s, %s, %s)")