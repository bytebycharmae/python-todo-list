# Mini Project: To-Do List

import random

# List that stores tasks
tasks = []

# Random productivity tips
tips = [
    "Start with the hardest task.",
    "Take short breaks.",
    "Stay organized.",
    "Work on one thing at a time."
]

# Function to add a task
def add_task():
    task_name = input("Enter a task: ")

    # Dictionary for a task
    task = {
        "name": task_name
    }

    tasks.append(task)
    print("Task added.")

# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for task in tasks:
            print("-", task["name"])

# Function to save tasks to a file
def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task["name"] + "\n")

    file.close()
    print("Tasks saved.")

# Function to load tasks from a file
def load_tasks():
    try:
        file = open("tasks.txt", "r")

        tasks.clear()

        for line in file:
            task = {
                "name": line.strip()
            }
            tasks.append(task)

        file.close()
        print("Tasks loaded.")

    except FileNotFoundError:
        print("No saved file found.")

# Function for random study tip
def random_tip():
    print(random.choice(tips))

# Main menu loop
running = True

while running:

    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save Tasks")
    print("4. Load Tasks")
    print("5. Random Study Tip")
    print("6. Exit")
    print("(Input Number)")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        save_tasks()

    elif choice == "4":
        load_tasks()

    elif choice == "5":
        random_tip()

    elif choice == "6":
        running = False
        print("Goodbye!")

    else:
        print("Invalid choice.")