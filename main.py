from services.student_services import *
from services.courses_services import *
from services.batches_services import *
from services.faculty_services import *


# ==========================================================
# MAIN PROGRAM
# ==========================================================

while True:

    print("\n===================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Student Management")
    print("2. Course Management")
    print("3. Batch Management")
    print("4. Faculty Management")
    print("5. Exit")

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
            print("6. Change Batch")
            print("7. Back to Main Menu")

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
                while True:
                    print("Update by:")
                    print("1.Update Student Name:")
                    print("2.Update Student Mobile:")
                    print("3.Update Student Email:")
                    print("4.Update Student Address:")
                    print("5.Update Student Admission Date:")
                    print("6.Update Course ID:")
                    print("7.Update Batch ID:")
                    print("8.Update all details:")
                    print("9.Back to sms menu")

                    ch= int(input("Enter the choice:"))
                    if ch==1:
                        update_name()
                    elif ch==2:
                        update_mobile()
                    elif ch==3:
                        update_email()
                    elif ch==4:
                        update_address()
                    elif ch==5:
                        update_admission_date()
                    elif ch==6:
                        update_course_id()
                    elif ch==7:
                        update_batch_id()
                    elif ch==8:
                        update_student()
                    else:
                        print("Exit from update, back to sms menu")
                        break;
            
            elif student_choice == 6:
                  change_batch()
                

            elif student_choice == 7:
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

                while True:

                    print("\n===================================")
                    print("        UPDATE COURSE")
                    print("===================================")
                    print("1. Update Course Name")
                    print("2. Update Duration")
                    print("3. Update Fees")
                    print("4. Update Complete Course")
                    print("5. Back")

                    try:
                        ch = int(input("Enter Your Choice: "))

                    except ValueError:
                        print("Please enter numbers only.")
                        continue

                    if ch == 1:
                        update_course_name()

                    elif ch == 2:
                        update_duration()

                    elif ch == 3:
                        update_fees()

                    elif ch == 4:
                        update_course()

                    elif ch == 5:
                        print("Back to cms menu")
                        break

                    else:
                        print("Invalid Choice.")

            elif course_choice == 6:
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid Choice. Please try again.")
    
    # ==========================================================
    # BATCH MANAGEMENT MENU
    # ==========================================================

    elif choice == 3:

        while True:

            print("\n===================================")
            print("       BATCH MANAGEMENT")
            print("===================================")
            print("1. Add Batch")
            print("2. Search Batch")
            print("3. Delete Batch")
            print("4. View Batch")
            print("5. Update Batch")
            print("6. Assign Faculty")
            print("7. Remove Faculty")
            print("8. View Batch Students")
            print("9. Back to Main Menu")

            # -------- COURSE MENU VALIDATION --------
            try:
                course_choice = int(input("Enter Your Choice: "))

            except ValueError:
                print("❌ Please enter numbers only.")
                continue

            # -------- CALL COURSE FUNCTIONS --------
            if course_choice == 1:
                add_batch()

            elif course_choice == 2:
                search_batch()

            elif course_choice == 3:
                delete_batch()

            elif course_choice == 4:
                view_batch()

            elif course_choice == 5:

                while True:

                    print("\n===================================")
                    print("        UPDATE BATCH")
                    print("===================================")
                    print("1. Update Batch Name")
                    print("2. Update Batch Timing")
                    print("3. Update Batch Start Date")
                    print("4. Update Course ID")
                    print("5. Update Complete Batch")
                    print("6. Back")

                    try:
                        ch = int(input("Enter Your Choice: "))

                    except ValueError:
                        print("Please enter numbers only.")
                        continue

                    if ch == 1:
                        update_batch_name()

                    elif ch == 2:
                        update_batch_timing()

                    elif ch == 3:
                        update_batch_start_date()

                    elif ch == 4:
                        update_batch_course()

                    elif ch == 5:
                        update_batch()

                    elif ch == 6:
                        print("Back to bms menu")
                        break

                    else:
                        print("Invalid Choice.")

            elif course_choice == 6:
                assign_faculty()

            elif course_choice == 7:
                remove_faculty()
            
            elif course_choice == 8:
                view_batch_students() 

            elif course_choice == 9:
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid Choice. Please try again.")

    
    # ==========================================================
    # FACULTY MANAGEMENT MENU
    # ==========================================================

    elif choice == 4:

        while True:

            print("\n===================================")
            print("       FACULTY MANAGEMENT")
            print("===================================")
            print("1. Add Faculty")
            print("2. Search Faculty")
            print("3. Delete Faculty")
            print("4. View Faculty")
            print("5. Update Faculty")
            print("6. Assign Batch")
            print("7. View Faculty Batches")
            print("8. Back to Main Menu")

            # -------- FACULTY MENU VALIDATION --------
            try:
                faculty_choice = int(input("Enter Your Choice: "))

            except ValueError:
                print("❌ Please enter numbers only.")
                continue

            # -------- CALL FACULTY FUNCTIONS --------
            if faculty_choice == 1:
                add_faculty()

            elif faculty_choice == 2:
                search_faculty()

            elif faculty_choice == 3:
                delete_faculty()

            elif faculty_choice == 4:
                view_faculty()

            elif faculty_choice == 5:

                while True:

                    print("\n===================================")
                    print("        UPDATE FACULTY")
                    print("===================================")
                    print("1. Update Faculty Name")
                    print("2. Update Faculty Mobile")
                    print("3. Update Faculty Email")
                    print("4. Update Faculty Skill")
                    print("5. Update Faculty Joining Date")
                    print("6. Update Complete Faculty")
                    print("7. Back")

                    try:
                        ch = int(input("Enter Your Choice: "))

                    except ValueError:
                        print("❌ Please enter numbers only.")
                        continue

                    if ch == 1:
                        update_faculty_name()

                    elif ch == 2:
                        update_faculty_mobile()

                    elif ch == 3:
                        update_faculty_email()

                    elif ch == 4:
                        update_faculty_skill()

                    elif ch == 5:
                        update_faculty_joining_date()

                    elif ch == 6:
                        update_faculty()

                    elif ch == 7:
                        print("Returning to Faculty Menu...")
                        break

                    else:
                        print("❌ Invalid Choice.")
            
            elif faculty_choice==6:
                assign_batch()

            elif faculty_choice==7:
                view_faculty_batches()

            elif faculty_choice == 8:
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid Choice. Please try again.")

    # ==========================================================
    # EXIT PROGRAM
    # ==========================================================
    elif choice == 5:
        print("\n✅ Thank You for using the Student Management System.")
        break

    # -------- INVALID MAIN MENU CHOICE --------
    else:
        print("❌ Invalid Choice. Please select between 1 and 3.")