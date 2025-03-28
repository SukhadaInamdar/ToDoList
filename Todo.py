import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task_id, description, deadline, status = line.strip().split(", ")
                tasks.append({"id": int(task_id), "description": description, "deadline": deadline, "status": status})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}, {task['description']}, {task['deadline']}, {task['status']}\n")

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = len(tasks) + 1  # Assign the next task ID
    tasks.append({"id": task_id, "description": description, "deadline": deadline, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")
    print(f"(Task saved to {TASKS_FILE})")

# View all tasks
def view_tasks(tasks):
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    completed_tasks = [task for task in tasks if task["status"] == "Completed"]

    print("\nTo-Do List:")
    print("[Pending]")
    if pending_tasks:
        for task in pending_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("No pending tasks.")

    print("\n[Completed]")
    if completed_tasks:
        for task in completed_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("No tasks completed yet.")

# Edit a task
def edit_task(tasks):
    task_id = int(input("Enter task number to edit: "))
    task = next((task for task in tasks if task["id"] == task_id), None)
    
    if task:
        print(f"Editing task: {task['description']}")
        task["description"] = input("Enter new description: ")
        task["deadline"] = input("Enter new deadline (YYYY-MM-DD): ")
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Task not found.")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task number to delete: "))
    task = next((task for task in tasks if task["id"] == task_id), None)
    
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Task not found.")

# Mark a task as completed
def mark_completed(tasks):
    task_id = int(input("Enter task number to mark as completed: "))
    task = next((task for task in tasks if task["id"] == task_id), None)
    
    if task:
        task["status"] = "Completed"
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Task not found.")

# Display the main menu and get user's choice
def display_menu():
    print("\nWelcome to To-Do List Manager!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main function to run the program
def main():
    tasks = load_tasks()

    while True:
        choice = display_menu()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
