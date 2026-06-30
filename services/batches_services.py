from database.db import *
from models.batches import batches


#add
def add_batch():
    conn= get_connection()
    cursor= conn.cursor()

    batch_name= input("Enter batch name:")
    timing= input("Enter batch time(M/E):")
    start_date=input("Enter startdate (yyyy-mm-dd):")
    course_id=int(input("Enter course id:"))

    b= batches(batch_name, timing, start_date, course_id)

    cursor.execute("insert into batches(batch_name, timing, start_date, course_id) values (%s,%s, %s, %s)", (b.batch_name, b.timing, b.start_date, b.course_id))
    conn.commit()
    print("Batch Added !")


# ==========================================================
# SEARCH BATCH
# ==========================================================
def search_batch():

    # ---------------- Batch ID Validation ----------------
    try:
        batch_id = int(input("Enter Batch ID to search: "))

        if batch_id <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Search Batch ----------------
        cursor.execute("""
        SELECT *
        FROM batches
        WHERE batch_id=%s
        """, (batch_id,))

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\n===================================")
        print("          BATCH DETAILS")
        print("===================================")
        print("Batch ID     :", row[0])
        print("Batch Name   :", row[1])
        print("Timing       :", row[2])
        print("Start Date   :", row[3])
        print("Course ID    :", row[4])

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# DELETE BATCH
# ==========================================================
def delete_batch():

    # ---------------- Batch ID Validation ----------------
    try:
        batch_id = int(input("Enter Batch ID to delete: "))

        if batch_id <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Check Batch Exists ----------------
        cursor.execute("""
        SELECT *
        FROM batches
        WHERE batch_id=%s
        """, (batch_id,))

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nBatch Found")
        print("-----------------------------------")
        print("Batch ID    :", row[0])
        print("Batch Name  :", row[1])
        print("Timing      :", row[2])
        print("Start Date  :", row[3])
        print("Course ID   :", row[4])

        # ---------------- Confirmation ----------------
        choice = input("\nAre you sure you want to delete this batch? (Y/N): ").strip().upper()

        if choice != "Y":
            print("Delete operation cancelled.")
            return

        # ---------------- Delete Batch ----------------
        cursor.execute("""
        DELETE FROM batches
        WHERE batch_id=%s
        """, (batch_id,))

        conn.commit()

        print("Batch deleted successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()




# ==========================================================
# VIEW ALL BATCHES
# ==========================================================
def view_batch():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT *
        FROM batches
        ORDER BY batch_id
        """)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No batches available.")
            return

        print("\n==============================================")
        print("              BATCH LIST")
        print("==============================================")

        for row in rows:

            print("----------------------------------------------")
            print("Batch ID    :", row[0])
            print("Batch Name  :", row[1])
            print("Timing      :", row[2])
            print("Start Date  :", row[3])
            print("Course ID   :", row[4])

    except Exception as e:
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

# ==========================================================
# UPDATE BATCH
# ==========================================================
def update_batch():

    # ---------------- Batch ID Validation ----------------
    try:
        batch_id = int(input("Enter Batch ID to update: "))

        if batch_id <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ---------------- Check Batch Exists ----------------
        cursor.execute("""
        SELECT *
        FROM batches
        WHERE batch_id=%s
        """, (batch_id,))

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nCurrent Batch Details")
        print("-----------------------------------")
        print("Batch Name :", row[1])
        print("Timing     :", row[2])
        print("Start Date :", row[3])
        print("Course ID  :", row[4])

        print("\nEnter New Details")

        # ---------------- Batch Name Validation ----------------
        batch_name = input("Enter Batch Name: ").strip()

        if batch_name == "":
            print("Batch name cannot be empty.")
            return

        # ---------------- Timing Validation ----------------
        timing = input("Enter Timing (M/E): ").strip().upper()

        if timing not in ("M", "E"):
            print("Timing must be M or E.")
            return

        # ---------------- Start Date Validation ----------------
        start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()

        if start_date == "":
            print("Start date cannot be empty.")
            return

        # ---------------- Course ID Validation ----------------
        try:
            course_id = int(input("Enter Course ID: "))

            if course_id <= 0:
                print("Course ID must be greater than 0.")
                return

        except ValueError:
            print("Course ID must be numeric.")
            return

        # ---------------- Check Course Exists ----------------
        cursor.execute("""
        SELECT *
        FROM courses
        WHERE course_id=%s
        """, (course_id,))

        if cursor.fetchone() is None:
            print("Course ID does not exist.")
            return

        # ---------------- Update Batch ----------------
        cursor.execute("""
        UPDATE batches
        SET batch_name=%s,
            timing=%s,
            start_date=%s,
            course_id=%s
        WHERE batch_id=%s
        """, (batch_name, timing, start_date, course_id, batch_id))

        conn.commit()

        print("Batch updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


def update_batch_name():

    try:
        bid = int(input("Enter Batch ID to update batch name: "))

        if bid <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM batches WHERE batch_id=%s",
            (bid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nCurrent Batch Name :", row[1])

        name = input("Enter New Batch Name: ").strip()

        if name == "":
            print("Batch name cannot be empty.")
            return

        if name == row[1]:
            print("New batch name is same as current.")
            return

        cursor.execute(
            "UPDATE batches SET batch_name=%s WHERE batch_id=%s",
            (name, bid)
        )

        conn.commit()

        print("Batch name updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()

def update_batch_timing():

    try:
        bid = int(input("Enter Batch ID to update timing: "))

        if bid <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM batches WHERE batch_id=%s",
            (bid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nCurrent Timing :", row[2])

        timing = input("Enter Timing (M/E): ").upper().strip()

        if timing not in ("M", "E"):
            print("Timing must be M or E.")
            return

        if timing == row[2]:
            print("Timing is already the same.")
            return

        cursor.execute(
            "UPDATE batches SET timing=%s WHERE batch_id=%s",
            (timing, bid)
        )

        conn.commit()

        print("Batch timing updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


from datetime import datetime

def update_batch_start_date():

    try:
        bid = int(input("Enter Batch ID to update start date: "))

        if bid <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM batches WHERE batch_id=%s",
            (bid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nCurrent Start Date :", row[3])

        start_date = input("Enter New Start Date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        if str(row[3]) == start_date:
            print("Start date is already the same.")
            return

        cursor.execute(
            "UPDATE batches SET start_date=%s WHERE batch_id=%s",
            (start_date, bid)
        )

        conn.commit()

        print("Batch start date updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


def update_batch_course():

    try:
        bid = int(input("Enter Batch ID to update Course ID: "))

        if bid <= 0:
            print("Batch ID must be greater than 0.")
            return

    except ValueError:
        print("Batch ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM batches WHERE batch_id=%s",
            (bid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Batch not found.")
            return

        print("\nCurrent Course ID :", row[4])

        try:
            cid = int(input("Enter New Course ID: "))

            if cid <= 0:
                print("Course ID must be greater than 0.")
                return

        except ValueError:
            print("Course ID must be numeric.")
            return

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (cid,)
        )

        if cursor.fetchone() is None:
            print("Course not found.")
            return

        cursor.execute(
            "UPDATE batches SET course_id=%s WHERE batch_id=%s",
            (cid, bid)
        )

        conn.commit()

        print("Batch course updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


def assign_faculty():
    
    batch_id= int(input("Enter batch ID to which we want to assign the faculty:"))
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


def remove_faculty():
    
    batch_id= int(input("Enter batch ID whose faculty should be removed:"))
    

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("select * from batches where batch_id=%s", (batch_id,))
    row1= cursor.fetchone()

    
    
    if(row1 is None ):
        print("Batch not found")
    else:
        cursor.execute(
            "UPDATE batches SET faculty_id = NULL WHERE batch_id = %s",
            (batch_id,)
        )
        conn.commit()
        print("Faculty removed !")


def view_batch_students() :
    batch_id = int(input("Enter the batch id whose students are to be displayed: "))

    conn= get_connection()
    cursor= conn.cursor()

    cursor.execute("select * from students where batch_id=%s", (batch_id,))
    rows= cursor.fetchall()

    for row in rows:
        print(row)