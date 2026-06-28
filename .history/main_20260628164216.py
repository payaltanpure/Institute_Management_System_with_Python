from services.student_services import *
from services.course_services import *

# ==========================================================
# MAIN PROGRAM
# ==========================================================

while True:

    print("\n===================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Student Management")
    print("2. Course Management")
    print("3. Exit")

    # -------- MAIN MENU VALIDATION --------
    try:
        choice = int(input("Enter Your Choice: "))

    except ValueError:
        print("❌ Please enter numbers only.")
        continue

    # ==========================================================
    # STUDENT MANAGEMENT MENU
    # ==========================================================
    if choice == 1:

        while True:

            print("\n===================================")
            print("      STUDENT MANAGEMENT")
            print("===================================")
            print("1. Add Student")
            print("2. Search Student")
            print("3. Delete Student")
            print("4. View Students")
            print("5. Update Student")
            print("6. Back to Main Menu")

            # -------- STUDENT MENU VALIDATION --------
            try:
                student_choice = int(input("Enter Your Choice: "))

            except ValueError:
                print("❌ Please enter numbers only.")
                continue

            # -------- CALL STUDENT FUNCTIONS --------
            if student_choice == 1:
                add_students()

            elif student_choice == 2:
                search_student()

            elif student_choice == 3:
                delete_student()

            elif student_choice == 4:
                view_students()

            elif student_choice == 5:
                update_student()

            elif student_choice == 6:
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid Choice. Please try again.")

    # ==========================================================
    # COURSE MANAGEMENT MENU
    # ==========================================================
    elif choice == 2:

        while True:

            print("\n===================================")
            print("       COURSE MANAGEMENT")
            print("===================================")
            print("1. Add Course")
            print("2. Search Course")
            print("3. Delete Course")
            print("4. View Courses")
            print("5. Update Course")
            print("6. Back to Main Menu")

            # -------- COURSE MENU VALIDATION --------
            try:
                course_choice = int(input("Enter Your Choice: "))

            except ValueError:
                print("❌ Please enter numbers only.")
                continue

            # -------- CALL COURSE FUNCTIONS --------
            if course_choice == 1:
                add_course()

            elif course_choice == 2:
                search_course()

            elif course_choice == 3:
                delete_course()

            elif course_choice == 4:
                view_courses()

            elif course_choice == 5:
                update_course()

            elif course_choice == 6:
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid Choice. Please try again.")

    # ==========================================================
    # EXIT PROGRAM
    # ==========================================================
    elif choice == 3:
        print("\n✅ Thank You for using the Student Management System.")
        break

    # -------- INVALID MAIN MENU CHOICE --------
    else:
        print("❌ Invalid Choice. Please select between 1 and 3.")