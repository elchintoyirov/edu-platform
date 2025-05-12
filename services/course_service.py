import json
import os
from uuid import uuid4

COURSES_FILE = 'data/courses.json'

def load_courses():
    if not os.path.exists(COURSES_FILE):
        return []
    with open(COURSES_FILE, 'r') as f:
        return json.load(f)

def save_courses(courses):
    with open(COURSES_FILE, 'w') as f:
        json.dump(courses, f, indent=4)

def create_course(teacher):
    print("\n--- Create New Course ---")
    title = input("Course title: ").strip()
    description = input("Course description: ").strip()
    price = float(input("Course price ($): ").strip())

    courses = load_courses()
    course = {
        "id": str(uuid4()),
        "title": title,
        "description": description,
        "price": price,
        "teacher_id": teacher["id"],
        "students": []
    }
    courses.append(course)
    save_courses(courses)
    print("Course created successfully!")

def list_courses_by_teacher(teacher):
    print("\n--- My Courses ---")
    courses = load_courses()
    found = False
    for course in courses:
        if course["teacher_id"] == teacher["id"]:
            found = True
            print(f"- {course['title']} (${course['price']}) | Students: {len(course['students'])}")
    if not found:
        print("You have no courses yet.")

def change_course_price(teacher):
    courses = load_courses()
    print("\n--- Change Course Price ---")
    my_courses = [c for c in courses if c["teacher_id"] == teacher["id"]]
    if not my_courses:
        print("You have no courses.")
        return

    for idx, course in enumerate(my_courses):
        print(f"{idx + 1}. {course['title']} (${course['price']})")

    choice = int(input("Select course number: ")) - 1
    if 0 <= choice < len(my_courses):
        new_price = float(input("Enter new price: "))
        my_courses[choice]["price"] = new_price
        save_courses(courses)
        print("Price updated.")
    else:
        print("Invalid choice.")

def view_course_students(teacher):
    courses = load_courses()
    print("\n--- View Students ---")
    for course in courses:
        if course["teacher_id"] == teacher["id"]:
            print(f"\n📘 {course['title']} ({len(course['students'])} students):")
            for student in course["students"]:
                print(f" - {student['name']} ({student['email']})")

def list_all_courses():
    print("\n--- All Available Courses ---")
    courses = load_courses()
    if not courses:
        print("No courses available.")
    for idx, course in enumerate(courses):
        print(f"{idx + 1}. {course['title']} - ${course['price']} | by Teacher ID: {course['teacher_id']}")

def buy_course(student):
    courses = load_courses()
    print("\n--- Buy Course ---")
    for idx, course in enumerate(courses):
        print(f"{idx + 1}. {course['title']} - ${course['price']}")
    if not courses:
        return
    choice = int(input("Select course number to buy: ")) - 1

    if 0 <= choice < len(courses):
        selected = courses[choice]
        for s in selected["students"]:
            if s["id"] == student["id"]:
                print("You already bought this course.")
                return
        selected["students"].append({
            "id": student["id"],
            "name": student["name"],
            "email": student["email"]
        })
        save_courses(courses)
        print("Course purchased successfully!")
    else:
        print("Invalid choice.")

def list_student_courses(student):
    print("\n--- My Purchased Courses ---")
    courses = load_courses()
    found = False
    for course in courses:
        if any(s["id"] == student["id"] for s in course["students"]):
            found = True
            print(f"- {course['title']} by Teacher ID: {course['teacher_id']}")
    if not found:
        print("You haven't purchased any courses yet.")
