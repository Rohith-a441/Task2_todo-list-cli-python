import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save the list of tasks back to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("\n📝 No tasks found.\n")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

def add_task(tasks):
    """Add a new task entered by the user."""
    new_task = input("Enter the task to add: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")
    else:
        print("⚠ Task cannot be empty!\n")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑 Task '{removed}' removed successfully!\n")
        else:
            print("⚠ Invalid task number!\n")
    except ValueError:
        print("⚠ Please enter a valid number!\n")

def main():
    print("===== 🧠 Welcome to Your Console To-Do List App! =====\n")
    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
