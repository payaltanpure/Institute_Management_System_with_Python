from database.db import get_connection
from models.courses import courses

#add course
def add_course():
    conn= get_connection()
    cursor= conn.cursor()

    ch= int(input("Enter how many courses you want to add:"))

    for i in range(1, ch+1):
        course_name = input("Enter course name:")
        duration= input("Enter duration:")
        fees= float(input("Enter fees")) 

        c= courses(course_name,duration, fees)

        query= ("insert into courses(course_name, duration, fees) values(%s, %s, %s)")
        values=(c.course_name, c.duration,c.fees)
        cursor.execute(query, values)
        conn.commit()

        print(f"Course {i} added!") 


def search_course():
    ch= int(input("Enter course_id to search the course:"))

    conn= get_connection()
    cursor= conn.cursor()

    cursor.execute("select * from courses where course_id=%s", (ch,))
    row= cursor.fetchone()
    print(row)

    if(cursor.rowcount>0):
        print("Course found")
    else:
        print("Course not available")


def delete_course():
    ch= int(input("Enter course_id to delete the course:"))

    conn= get_connection()
    cursor= conn.cursor()

    



