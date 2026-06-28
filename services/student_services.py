import re
from datetime import datetime

from database.db import get_connection
from models.student import student


# ==========================================================
# ADD STUDENT
# ==========================================================
def add_students():

    # ---------------- Student Name ----------------
    student_name = input("Enter Student Name: ").strip()

    if student_name == "":
        print("Student name cannot be empty.")
        return

    if not student_name.replace(" ", "").isalpha():
        print("Student name should contain only alphabets.")
        return

    # ---------------- Mobile ----------------
    tmobile = input("Enter Mobile Number: ").strip()

    if tmobile == "":
        print("Mobile number cannot be empty.")
        return

    if not tmobile.isdigit():
        print("Mobile number should contain digits only.")
        return

    if len(tmobile) != 10:
        print("Mobile number must contain exactly 10 digits.")
        return

    if tmobile[0] not in "6789":
        print("Mobile number must start with 6, 7, 8 or 9.")
        return

    # ---------------- Email ----------------
    email = input("Enter Email: ").strip()

    if email == "":
        print("Email cannot be empty.")
        return

    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(email_pattern, email):
        print("Invalid email format.")
        return

    # ---------------- Address ----------------
    address = input("Enter Address: ").strip()

    if address == "":
        print("Address cannot be empty.")
        return

    # ---------------- Admission Date ----------------
    admission_date = input("Enter Admission Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(admission_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return

    # Create Student Object
    s = student(
        student_name,
        tmobile,
        email,
        address,
        admission_date
    )

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Duplicate Mobile Check ----------------
        cursor.execute(
            "SELECT student_id FROM students WHERE mobile=%s",
            (tmobile,)
        )

        if cursor.fetchone():
            print("Mobile number already exists.")
            return

        # ---------------- Duplicate Email Check ----------------
        cursor.execute(
            "SELECT student_id FROM students WHERE email=%s",
            (email,)
        )

        if cursor.fetchone():
            print("Email already registered.")
            return

        # ---------------- Insert Student ----------------
        query = """
        INSERT INTO students
        (student_name, mobile, email, address, admission_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            s.student_name,
            s.mobile,
            s.email,
            s.address,
            s.admission_date
        )

        cursor.execute(query, values)

        conn.commit()

        print("Student added successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

# ==========================================================
# VIEW ALL STUDENTS
# ==========================================================
def view_students():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT student_id,
               student_name,
               mobile,
               email,
               address,
               admission_date
        FROM students
        ORDER BY student_id
        """)

        rows = cursor.fetchall()

        if not rows:
            print("\nNo students found.")
            return

        print("\n" + "=" * 80)
        print("                    STUDENT LIST")
        print("=" * 80)

        for row in rows:

            print(f"""
Student ID      : {row[0]}
Student Name    : {row[1]}
Mobile Number   : {row[2]}
Email           : {row[3]}
Address         : {row[4]}
Admission Date  : {row[5]}
{"-" * 80}
""")

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# SEARCH STUDENT
# ==========================================================
def search_student():

    try:
        sid = int(input("Enter Student ID: "))

        if sid <= 0:
            print("Student ID must be greater than zero.")
            return

    except ValueError:
        print("Student ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT student_id,
               student_name,
               mobile,
               email,
               address,
               admission_date
        FROM students
        WHERE student_id=%s
        """, (sid,))

        row = cursor.fetchone()

        if row:

            print("\n" + "=" * 50)
            print("        STUDENT FOUND")
            print("=" * 50)

            print(f"Student ID      : {row[0]}")
            print(f"Student Name    : {row[1]}")
            print(f"Mobile Number   : {row[2]}")
            print(f"Email           : {row[3]}")
            print(f"Address         : {row[4]}")
            print(f"Admission Date  : {row[5]}")

            print("=" * 50)

        else:
            print("No student found with ID", sid)

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

# ==========================================================
# DELETE STUDENT
# ==========================================================
def delete_student():

    try:
        sid = int(input("Enter Student ID to delete: "))

        if sid <= 0:
            print("Student ID must be greater than 0.")
            return

    except ValueError:
        print("Student ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Check Student Exists ----------------
        cursor.execute(
            """
            SELECT student_id, student_name
            FROM students
            WHERE student_id=%s
            """,
            (sid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("No student found with ID", sid)
            return

        print("\nStudent Found")
        print("---------------------------")
        print("Student ID   :", row[0])
        print("Student Name :", row[1])

        # ---------------- Confirmation ----------------
        choice = input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()

        if choice != "Y":
            print("Delete operation cancelled.")
            return

        # ---------------- Delete Student ----------------
        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (sid,)
        )

        conn.commit()

        print("Student deleted successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

# ==========================================================
# UPDATE STUDENT
# ==========================================================
def update_student():

    try:
        sid = int(input("Enter Student ID to update: "))

        if sid <= 0:
            print("Student ID must be greater than 0.")
            return

    except ValueError:
        print("Student ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Check Student Exists ----------------
        cursor.execute("""
        SELECT *
        FROM students
        WHERE student_id=%s
        """, (sid,))

        row = cursor.fetchone()

        if row is None:
            print("Student not found.")
            return

        print("\nCurrent Student Details")
        print("-----------------------------------")
        print("ID             :", row[0])
        print("Name           :", row[1])
        print("Mobile         :", row[2])
        print("Email          :", row[3])
        print("Address        :", row[4])
        print("Admission Date :", row[5])

        print("\nEnter New Details")

        # ---------------- Name Validation ----------------
        name = input("New Name: ").strip()

        if name == "":
            print("Student name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Student name should contain only alphabets.")
            return

        # ---------------- Mobile Validation ----------------
        mobile = input("New Mobile: ").strip()

        if mobile == "":
            print("Mobile number cannot be empty.")
            return

        if not mobile.isdigit():
            print("Mobile number should contain digits only.")
            return

        if len(mobile) != 10:
            print("Mobile number must contain exactly 10 digits.")
            return

        if mobile[0] not in "6789":
            print("Mobile number must start with 6, 7, 8 or 9.")
            return

        # ---------------- Email Validation ----------------
        email = input("New Email: ").strip()

        if email == "":
            print("Email cannot be empty.")
            return

        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.match(email_pattern, email):
            print("Invalid email format.")
            return

        # ---------------- Address Validation ----------------
        address = input("New Address: ").strip()

        if address == "":
            print("Address cannot be empty.")
            return

        # ---------------- Admission Date Validation ----------------
        admission_date = input("New Admission Date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(admission_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
            return
        
                # ---------------- Duplicate Mobile Check ----------------
        cursor.execute(
            """
            SELECT student_id
            FROM students
            WHERE mobile=%s
            AND student_id<>%s
            """,
            (mobile, sid)
        )

        if cursor.fetchone():
            print("Mobile number already exists.")
            return

        # ---------------- Duplicate Email Check ----------------
        cursor.execute(
            """
            SELECT student_id
            FROM students
            WHERE email=%s
            AND student_id<>%s
            """,
            (email, sid)
        )

        if cursor.fetchone():
            print("Email already registered.")
            return

        # ---------------- Update Student ----------------
        query = """
        UPDATE students
        SET
            student_name=%s,
            mobile=%s,
            email=%s,
            address=%s,
            admission_date=%s
        WHERE student_id=%s
        """

        values = (
            name,
            mobile,
            email,
            address,
            admission_date,
            sid
        )

        cursor.execute(query, values)

        conn.commit()

        print("\nStudent updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()