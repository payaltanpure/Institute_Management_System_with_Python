# Import all CRUD functions from student_services.py
from services.student_services import *

# # Infinite loop so menu keeps showing until user exits
# while True:

#     print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
#     print("1. Add Student")
#     print("2. Search Student")
#     print("3. Delete Student")
#     print("4. View Students")
#     print("5. Update Student")
#     print("6. Exit")
#     print("===============================================")

#     # ---------------- MENU VALIDATION ----------------
#     # Check whether user entered a number or not
#     try:
#         choice = int(input("Enter your choice (1-6): "))

#     except ValueError:
#         print("\n❌ Invalid Input!")
#         print("Please enter numbers only.")
#         continue       # Show menu again

#     # ----------- RANGE VALIDATION -----------------
#     # User entered a number but not between 1 and 6
#     if choice < 1 or choice > 6:
#         print("\n❌ Choice must be between 1 and 6.")
#         continue

#     # ---------------- MENU -----------------

#     if choice == 1:
#         add_students()

#     elif choice == 2:
#         search_student()

#     elif choice == 3:
#         delete_student()

#     elif choice == 4:
#         view_students()

#     elif choice == 5:
#         update_student()

#     elif choice == 6:
#         print("\nThank You!")
#         print("Exiting Student Management System...")
#         break
    

from services.course_services import *
add_course()