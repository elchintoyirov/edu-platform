import json
import os
from uuid import uuid4

USERS_FILE = 'data/users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)
    
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def email_exists(email, users):
    return any(user["email"] == email for user in users)

def register_user():
    print("Register")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter a password: ").strip()
    role = input("Are you a teacher: ").strip()

    users = load_users()

    if email_exists(email, users):
        print("Email is already registered!")
        return 
    
    user = {
        "id":str(uuid4()),
        "name":name,
        "email":email,
        "password":password,
        "is_teacher":role == "y"
    }

    users.append(user)
    save_users(users)
    print("Registration successful!")

def login_user():
    print("Login")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    users = load_users()

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome, {user['name']}!")
            return user

    print("Invalid credentials")
    return Nonef