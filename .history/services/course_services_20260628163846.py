from database.db import get_connection
from models.courses import courses

#add course
def add_course():
    conn= get_connection()
    cursor= conn.cursor()

    course_name = input("Enter course name:")
    duration= input("Enter duration:")
    fees= float(input("Enter fees"))

    c= courses(course_name,duration, fees)

    query= ("insert into courses(course_name, duration, fees) values(%s, %s, %s)")
    values=(c.course_name, c.duration,c.fees)
    cursor.execute(query, values)
    conn.commit()
    print("Course added!")