from database.db import *
from models.faculty import faculty
import re
from datetime import datetime

# ==========================================================
# ADD FACULTY
# ==========================================================
def add_faculty():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        while True:

            # ---------------- Faculty Name ----------------
            name = input("Enter Faculty Name: ").strip()

            if name == "":
                print("Faculty name cannot be empty.")
                continue

            if not name.replace(" ", "").isalpha():
                print("Faculty name should contain only alphabets.")
                continue

            # ---------------- Mobile ----------------
            mobile = input("Enter Mobile Number: ").strip()

            if mobile == "":
                print("Mobile number cannot be empty.")
                continue

            if not mobile.isdigit():
                print("Mobile number should contain digits only.")
                continue

            if len(mobile) != 10:
                print("Mobile number must contain exactly 10 digits.")
                continue

            if mobile[0] not in "6789":
                print("Mobile number must start with 6, 7, 8 or 9.")
                continue

            cursor.execute(
                "SELECT * FROM faculty WHERE mobile=%s",
                (mobile,)
            )

            if cursor.fetchone():
                print("Mobile number already exists.")
                continue

            # ---------------- Email ----------------
            email = input("Enter Email: ").strip()

            if email == "":
                print("Email cannot be empty.")
                continue

            pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

            if not re.match(pattern, email):
                print("Invalid email format.")
                continue

            cursor.execute(
                "SELECT * FROM faculty WHERE email=%s",
                (email,)
            )

            if cursor.fetchone():
                print("Email already exists.")
                continue

            # ---------------- Skill ----------------
            skill = input("Enter Skill: ").strip()

            if skill == "":
                print("Skill cannot be empty.")
                continue

            # ---------------- Joining Date ----------------
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

            if joining_date == "":
                print("Joining date cannot be empty.")
                continue

            try:
                datetime.strptime(joining_date, "%Y-%m-%d")

            except ValueError:
                print("Invalid date format.")
                continue

            # ---------------- Insert ----------------
            f = faculty(
                name,
                mobile,
                email,
                skill,
                joining_date
            )

            cursor.execute("""
                INSERT INTO faculty
                (faculty_name,mobile,email,skill,joining_date)
                VALUES(%s,%s,%s,%s,%s)
            """,
            (
                f.faculty_name,
                f.mobile,
                f.email,
                f.skill,
                f.joining_date
            ))

            conn.commit()

            print("Faculty Added Successfully.")
            break

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# SEARCH FACULTY
# ==========================================================
def search_faculty():

    try:
        faculty_id = int(input("Enter Faculty ID to search: "))

        if faculty_id <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (faculty_id,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\n===================================")
        print("        FACULTY DETAILS")
        print("===================================")
        print("Faculty ID     :", row[0])
        print("Faculty Name   :", row[1])
        print("Mobile         :", row[2])
        print("Email          :", row[3])
        print("Skill          :", row[4])
        print("Joining Date   :", row[5])

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# DELETE FACULTY
# ==========================================================
def delete_faculty():

    try:
        faculty_id = int(input("Enter Faculty ID to delete: "))

        if faculty_id <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (faculty_id,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nFaculty Found")
        print("--------------------------------")
        print("Faculty Name :", row[1])
        print("Mobile       :", row[2])
        print("Email        :", row[3])
        print("Skill        :", row[4])
        print("Joining Date :", row[5])

        ch = input("\nAre you sure? (Y/N): ").upper()

        if ch != "Y":
            print("Delete cancelled.")
            return

        cursor.execute("""
        DELETE FROM faculty
        WHERE faculty_id=%s
        """, (faculty_id,))

        conn.commit()

        print("Faculty deleted successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# VIEW FACULTY
# ==========================================================
def view_faculty():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        ORDER BY faculty_id
        """)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No faculty found.")
            return

        print("\n==============================================")
        print("              FACULTY LIST")
        print("==============================================")

        for row in rows:

            print("----------------------------------------------")
            print("Faculty ID    :", row[0])
            print("Faculty Name  :", row[1])
            print("Mobile        :", row[2])
            print("Email         :", row[3])
            print("Skill         :", row[4])
            print("Joining Date  :", row[5])

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

import re

# ==========================================================
# UPDATE FACULTY NAME
# ==========================================================
def update_faculty_name():

    try:
        fid = int(input("Enter Faculty ID to update name: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Faculty Name")
        print("--------------------------------")
        print("Name :", row[1])

        name = input("Enter New Name: ").strip()

        if name == "":
            print("Faculty name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Faculty name should contain only alphabets.")
            return

        if name == row[1]:
            print("New name is the same as current.")
            return

        cursor.execute("""
        UPDATE faculty
        SET faculty_name=%s
        WHERE faculty_id=%s
        """, (name, fid))

        conn.commit()

        print("Faculty name updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE FACULTY MOBILE
# ==========================================================
def update_faculty_mobile():

    try:
        fid = int(input("Enter Faculty ID to update mobile: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Mobile")
        print("--------------------------------")
        print("Mobile :", row[2])

        mobile = input("Enter New Mobile: ").strip()

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

        if mobile == row[2]:
            print("New mobile number is the same as current.")
            return

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE mobile=%s
        AND faculty_id<>%s
        """, (mobile, fid))

        if cursor.fetchone():
            print("Mobile number already exists.")
            return

        cursor.execute("""
        UPDATE faculty
        SET mobile=%s
        WHERE faculty_id=%s
        """, (mobile, fid))

        conn.commit()

        print("Faculty mobile updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE FACULTY EMAIL
# ==========================================================
def update_faculty_email():

    try:
        fid = int(input("Enter Faculty ID to update email: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Email")
        print("--------------------------------")
        print("Email :", row[3])

        email = input("Enter New Email: ").strip()

        if email == "":
            print("Email cannot be empty.")
            return

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.match(pattern, email):
            print("Invalid email format.")
            return

        if email == row[3]:
            print("New email is the same as current.")
            return

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE email=%s
        AND faculty_id<>%s
        """, (email, fid))

        if cursor.fetchone():
            print("Email already exists.")
            return

        cursor.execute("""
        UPDATE faculty
        SET email=%s
        WHERE faculty_id=%s
        """, (email, fid))

        conn.commit()

        print("Faculty email updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

from datetime import datetime

# ==========================================================
# UPDATE FACULTY SKILL
# ==========================================================
def update_faculty_skill():

    try:
        fid = int(input("Enter Faculty ID to update skill: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Skill")
        print("--------------------------------")
        print("Skill :", row[4])

        skill = input("Enter New Skill: ").strip()

        if skill == "":
            print("Skill cannot be empty.")
            return

        if skill == row[4]:
            print("New skill is the same as current.")
            return

        cursor.execute("""
        UPDATE faculty
        SET skill=%s
        WHERE faculty_id=%s
        """, (skill, fid))

        conn.commit()

        print("Faculty skill updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE FACULTY JOINING DATE
# ==========================================================
def update_faculty_joining_date():

    try:
        fid = int(input("Enter Faculty ID to update joining date: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Joining Date")
        print("--------------------------------")
        print("Joining Date :", row[5])

        joining_date = input("Enter New Joining Date (YYYY-MM-DD): ").strip()

        if joining_date == "":
            print("Joining date cannot be empty.")
            return

        try:
            datetime.strptime(joining_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        if str(row[5]) == joining_date:
            print("New joining date is the same as current.")
            return

        cursor.execute("""
        UPDATE faculty
        SET joining_date=%s
        WHERE faculty_id=%s
        """, (joining_date, fid))

        conn.commit()

        print("Faculty joining date updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE COMPLETE FACULTY
# ==========================================================
def update_faculty():

    try:
        fid = int(input("Enter Faculty ID to update: "))

        if fid <= 0:
            print("Faculty ID must be greater than 0.")
            return

    except ValueError:
        print("Faculty ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE faculty_id=%s
        """, (fid,))

        row = cursor.fetchone()

        if row is None:
            print("Faculty not found.")
            return

        print("\nCurrent Faculty Details")
        print("--------------------------------")
        print("Faculty ID    :", row[0])
        print("Name          :", row[1])
        print("Mobile        :", row[2])
        print("Email         :", row[3])
        print("Skill         :", row[4])
        print("Joining Date  :", row[5])

        print("\nEnter New Details")

        # ---------------- Name ----------------
        name = input("Enter Faculty Name: ").strip()

        if name == "":
            print("Faculty name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Faculty name should contain only alphabets.")
            return

        # ---------------- Mobile ----------------
        mobile = input("Enter Mobile Number: ").strip()

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

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE mobile=%s
        AND faculty_id<>%s
        """, (mobile, fid))

        if cursor.fetchone():
            print("Mobile number already exists.")
            return

        # ---------------- Email ----------------
        email = input("Enter Email: ").strip()

        if email == "":
            print("Email cannot be empty.")
            return

        import re

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.match(pattern, email):
            print("Invalid email format.")
            return

        cursor.execute("""
        SELECT *
        FROM faculty
        WHERE email=%s
        AND faculty_id<>%s
        """, (email, fid))

        if cursor.fetchone():
            print("Email already exists.")
            return

        # ---------------- Skill ----------------
        skill = input("Enter Skill: ").strip()

        if skill == "":
            print("Skill cannot be empty.")
            return

        # ---------------- Joining Date ----------------
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

        if joining_date == "":
            print("Joining date cannot be empty.")
            return

        try:
            datetime.strptime(joining_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        cursor.execute("""
        UPDATE faculty
        SET faculty_name=%s,
            mobile=%s,
            email=%s,
            skill=%s,
            joining_date=%s
        WHERE faculty_id=%s
        """, (
            name,
            mobile,
            email,
            skill,
            joining_date,
            fid
        ))

        conn.commit()

        print("\nFaculty updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


#assign batch function
def assign_batch():
    batch_id= int(input("Enter batch ID to assign:"))
    faculty_id= int(input("Enter faculty ID to whom u want to assign the batch:"))

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("select * from batches where batch_id=%s", (batch_id,))
    row1= cursor.fetchone()

    cursor.execute("select * from faculty where faculty_id=%s", (faculty_id,))
    row2= cursor.fetchone()
    
    if(row1 is None or row2 is None):
        print("Batch of Faculty not found")
    else:
        cursor.execute("update batches set faculty_id=%s where batch_id=%s", (faculty_id, batch_id))
        conn.commit()
        print("Batch assigned to faculty!")


    
def view_faculty_batches():
    faculty_id = int(input("Enter faculty id whose batches u want to check:"))

    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("select * from batches where faculty_id=%s", (faculty_id,))
    rows= cursor.fetchall()
    cursor.execute("select * from faculty where faculty_id=%s", (faculty_id,))
    row1= cursor.fetchall()
    for row1 in row1:
        print(f"Faculty name: {row1[1]}") 
    for row in rows:
        print(f"Batch id: {row[0]}")
        print(f"Batch Name: {row[1]}")
        print(f"Timing: {row[2]}")
        print(f"Course ID: {row[4]}")

    


