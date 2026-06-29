from database.db import get_connection
from models.courses import courses


# ==========================================================
# ADD COURSE
# ==========================================================
def add_course():

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Validate number of courses
        try:
            count = int(input("Enter how many courses you want to add: "))

            if count <= 0:
                print("Number of courses must be greater than 0.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        # Loop to add courses
        for i in range(1, count + 1):

            print(f"\nEnter Details of Course {i}")

            # -----------------------------
            # Course Name Validation
            # -----------------------------
            course_name = input("Enter Course Name: ").strip()

            if course_name == "":
                print("Course name cannot be empty.")
                continue

            if not course_name.replace(" ", "").isalpha():
                print("Course name should contain only alphabets.")
                continue

            # -----------------------------
            # Duration Validation
            # -----------------------------
            duration = input("Enter Course Duration: ").strip()

            if duration == "":
                print("Duration cannot be empty.")
                continue

            # -----------------------------
            # Fees Validation
            # -----------------------------
            try:
                fees = float(input("Enter Course Fees: "))

                if fees <= 0:
                    print("Fees must be greater than 0.")
                    continue

            except ValueError:
                print("Fees must be numeric.")
                continue

            # Create Course Object
            c = courses(course_name, duration, fees)

            query = """
                    INSERT INTO courses(course_name, duration, fees)
                    VALUES(%s,%s,%s)
                    """

            values = (c.course_name, c.duration, c.fees)

            cursor.execute(query, values)
            conn.commit()

            print(f"Course {i} added successfully.")

    except Exception as e:
        print("Database Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ==========================================================
# SEARCH COURSE
# ==========================================================
def search_course():

    try:
        try:
            course_id = int(input("Enter Course ID to search: "))

            if course_id <= 0:
                print("Course ID must be greater than 0.")
                return

        except ValueError:
            print("Course ID must be numeric.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (course_id,)
        )

        row = cursor.fetchone()

        if row:

            print("\nCourse Found")
            print("------------------------")
            print("Course ID :", row[0])
            print("Course Name :", row[1])
            print("Duration :", row[2])
            print("Fees :", row[3])

        else:
            print("Course not found.")

    except Exception as e:
        print("Database Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ==========================================================
# DELETE COURSE
# ==========================================================
def delete_course():

    try:
        try:
            course_id = int(input("Enter Course ID to delete: "))

            if course_id <= 0:
                print("Course ID must be greater than 0.")
                return

        except ValueError:
            print("Course ID must be numeric.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        # Check if course exists
        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (course_id,)
        )

        if cursor.fetchone() is None:
            print("Course not found.")
            return

        cursor.execute(
            "DELETE FROM courses WHERE course_id=%s",
            (course_id,)
        )

        conn.commit()

        print("Course deleted successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ==========================================================
# VIEW ALL COURSES
# ==========================================================
def view_courses():

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM courses ORDER BY course_id"
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No courses available.")
            return

        print("\nCourse List")
        print("-" * 60)

        for row in rows:
            print(
                f"ID : {row[0]} | "
                f"Name : {row[1]} | "
                f"Duration : {row[2]} | "
                f"Fees : {row[3]}"
            )

    except Exception as e:
        print("Database Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ==========================================================
# UPDATE COURSE
# ==========================================================
def update_course():

    try:

        # -----------------------------
        # Course ID Validation
        # -----------------------------
        try:
            course_id = int(input("Enter Course ID to update: "))

            if course_id <= 0:
                print("Course ID must be greater than 0.")
                return

        except ValueError:
            print("Course ID must be numeric.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (course_id,)
        )

        row = cursor.fetchone()

        # Correct way to check record
        if row is None:
            print("Course not found.")
            return

        print("\nCurrent Course Details")
        print("----------------------")
        print("Course ID :", row[0])
        print("Course Name :", row[1])
        print("Duration :", row[2])
        print("Fees :", row[3])

        print("\nEnter New Details")

        # -----------------------------
        # Name Validation
        # -----------------------------
        name = input("Enter Course Name: ").strip()

        if name == "":
            print("Course name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Course name should contain only alphabets.")
            return

        # -----------------------------
        # Duration Validation
        # -----------------------------
        duration = input("Enter Duration: ").strip()

        if duration == "":
            print("Duration cannot be empty.")
            return

        # -----------------------------
        # Fees Validation
        # -----------------------------
        

        try:
            fees = float(input("Enter Fees: "))

            if fees <= 0:
                print("Fees must be greater than 0.")
                return

        except ValueError:
            print("Fees must be numeric.")
            return

        

        query = """
                UPDATE courses
                SET course_name=%s,
                    duration=%s,
                    fees=%s
                WHERE course_id=%s
                """

        values = (
            name,
            duration,
            fees,
            course_id
        )

        cursor.execute(query, values)

        conn.commit()

        print("\nCourse updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# ==========================================================
# UPDATE COURSE NAME
# ==========================================================
def update_course_name():

    try:
        cid = int(input("Enter Course ID to update course name: "))

        if cid <= 0:
            print("Course ID must be greater than 0.")
            return

    except ValueError:
        print("Course ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (cid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Course not found.")
            return

        print("\nCurrent Course Name :", row[1])

        name = input("Enter New Course Name: ").strip()

        if name == "":
            print("Course name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Course name should contain only alphabets.")
            return

        if name == row[1]:
            print("New course name is the same as current.")
            return

        cursor.execute(
            "UPDATE courses SET course_name=%s WHERE course_id=%s",
            (name, cid)
        )

        conn.commit()

        print("Course name updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE COURSE DURATION
# ==========================================================
def update_duration():

    try:
        cid = int(input("Enter Course ID to update duration: "))

        if cid <= 0:
            print("Course ID must be greater than 0.")
            return

    except ValueError:
        print("Course ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (cid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Course not found.")
            return

        print("\nCurrent Duration :", row[2])

        duration = input("Enter New Duration: ").strip()

        if duration == "":
            print("Duration cannot be empty.")
            return

        if duration == row[2]:
            print("New duration is the same as current.")
            return

        cursor.execute(
            "UPDATE courses SET duration=%s WHERE course_id=%s",
            (duration, cid)
        )

        conn.commit()

        print("Course duration updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()


# ==========================================================
# UPDATE COURSE FEES
# ==========================================================
def update_fees():

    try:
        cid = int(input("Enter Course ID to update fees: "))

        if cid <= 0:
            print("Course ID must be greater than 0.")
            return

    except ValueError:
        print("Course ID must be numeric.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM courses WHERE course_id=%s",
            (cid,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Course not found.")
            return

        print("\nCurrent Fees :", row[3])

        try:
            fees = float(input("Enter New Fees: "))

            if fees <= 0:
                print("Fees must be greater than 0.")
                return

        except ValueError:
            print("Fees must be numeric.")
            return

        if fees == row[3]:
            print("New fees are the same as current.")
            return

        cursor.execute(
            "UPDATE courses SET fees=%s WHERE course_id=%s",
            (fees, cid)
        )

        conn.commit()

        print("Course fees updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Database Error:", e)

    finally:
        cursor.close()
        conn.close()