from database.db import *
from models.courses import courses

#add course
def add_course():
    conn= get_connection()
    cursor= conn.cursor()

    couse