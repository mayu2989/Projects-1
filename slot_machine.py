import random
import time
import json
import os

# File to store user data
USER_DATA_FILE = "slot_machine_users.json"

# Slot machine items
items = {
    1: "apple", 2: "banana", 3: "grape", 4: "star",
    5: "red ball", 6: "green ball", 7: "blue ball", 8: "moon"
}

# Point system
POINT_RULES = {
    "all_same": 100,
    "all_stars": 200,
    "two_same": 50,
    "one_star": 20
}

# Function to load user data
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save user data
def save_user_data(user_data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file, indent=4)

# Function to authenticate user
def authenticate_user():
    user_data = load_user_data()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_data:
        if user_data[username]["password"] == password:
            print(f"Welcome back, {username}! Your current score: {user_data[username]['score']} points")
            return username, user_data
        else:
            print("Incorrect password! Try again.")
            return authenticate_user()
    else:
        print("New user detected! Creating account...")
        user_data[username] = {"password": password, "score": 0}
        save_user_data(user_data)
        print(f"Account created! Welcome, {username}. Your score is set to 0.")
        return username, user_data

# Function to run slot machine
def play_slot_machine(username, user_data):
    print("Welcome to the slot machine!")
    print("Points system:")
    print("1. If all are same → 100 points")
    print("2. If all are stars → 200 points")
    print("3. If any two are same → 50 points")
    print("4. If a star appears → 20 points")
    
    time.sleep(2)
    stop_time = int(input("Enter the stopping time in seconds: "))

    for _ in range(stop_time):
        slot_1, slot_2, slot_3 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
        print(f"[{items[slot_1]}] - [{items[slot_2]}] - [{items[slot_3]}]")
        time.sleep(1)

    # Score calculations
    result_items = [items[slot_1], items[slot_2], items[slot_3]] # type: ignore
    if result_items[0] == result_items[1] == result_items[2]:
        points = POINT_RULES["all_stars"] if result_items[0] == "star" else POINT_RULES["all_same"]
    elif result_items[0] == result_items[1] or result_items[1] == result_items[2] or result_items[0] == result_items[2]:
        points = POINT_RULES["two_same"]
    elif "star" in result_items:
        points = POINT_RULES["one_star"]
    else:
        points = 0

    # Update score
    user_data[username]["score"] += points
    save_user_data(user_data)

    # Display results
    print(f"\nYou scored {points} points!")
    print(f"Your updated score: {user_data[username]['score']} points")

# Main execution
username, user_data = authenticate_user()
play_slot_machine(username, user_data)