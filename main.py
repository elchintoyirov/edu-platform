from services.auth import register_user, login_user
from services.course_service import *
from services.messaging import *

def main_menu():
    print("""
    Welcome to the edu-platform
    1. Register
    2. Login
    3. Exit
    """)
    return input("Choose an option: ")

def teacher_menu(user):
    while True:
        print("""
        1. Create course
        2. View my courses
        3. Change course price
        4. View Students
        5. View Messages
        6. Log Out
        """)
        choice = input("Choose an option: ")
        if choice == "1":
            create_course(user)
        elif choice == "2":
            buy_course(user)
            list_student_courses(user)
        elif choice == "4":
            send_message(user)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def student_menu(user):
    while True:
        print(f"\n--- Student Menu ({user['name']}) ---")
        print("1. Browse Courses")
        print("2. Buy Course")
        print("3. My Courses")
        print("4. Message Teacher")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            list_all_courses()
        elif choice == "2":
            buy_course(user)
        elif choice == "3":
            list_student_courses(user)
        elif choice == "4":
            send_message(user)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def run():
    while True:
        choice = main_menu()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user["is_teacher"]:
                teacher_menu(user)
            else:
                student_menu(user)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
          
if __name__ == "__main__":
    run()