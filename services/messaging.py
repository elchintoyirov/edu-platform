import json
import os
from datetime import datetime
from uuid import uuid4
from services.auth import load_users

MESSAGES_FILE = 'data/messages.json'

def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    with open(MESSAGES_FILE, 'r') as f:
        return json.load(f)

def save_messages(messages):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=4)

def send_message(sender):
    print("\n--- Send Message to Teacher ---")
    teacher_email = input("Enter teacher's email: ").strip()
    users = load_users()

    teacher = next((u for u in users if u["email"] == teacher_email and u["is_teacher"]), None)
    if not teacher:
        print("Teacher not found.")
        return

    content = input("Enter your message: ").strip()
    message = {
        "id": str(uuid4()),
        "from_id": sender["id"],
        "from_name": sender["name"],
        "to_id": teacher["id"],
        "to_name": teacher["name"],
        "content": content,
        "timestamp": datetime.now().isoformat()
    }

    messages = load_messages()
    messages.append(message)
    save_messages(messages)
    print("Message sent successfully.")

def view_messages(receiver):
    print("\n--- My Messages ---")
    messages = load_messages()
    received = [m for m in messages if m["to_id"] == receiver["id"]]

    if not received:
        print("📭 No messages yet.")
        return

    for m in received:
        print(f"\n📨 From: {m['from_name']} ({m['timestamp']})")
        print(f"   {m['content']}")
