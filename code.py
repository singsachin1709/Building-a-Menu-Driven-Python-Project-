# Menu Driven To-Do List Manager

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print(f"✅ Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔ Done" if t["done"] else "❌ Not Done"
        print(f"{i}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to mark as done: "))
        tasks[choice-1]["done"] = True
        print("✅ Task marked as done!")
    except (ValueError, IndexError):
        print("⚠ Invalid choice.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice-1)
        print(f"🗑 Task '{removed['task']}' deleted!")
    except (ValueError, IndexError):
        print("⚠ Invalid choice.")

# Main loop
while True:
    show_menu()
    try:
        option = int(input("Choose an option (1-5): "))
    except ValueError:
        print("⚠ Please enter a number between 1-5.")
        continue

    if option == 1:
        add_task()
    elif option == 2:
        view_tasks()
    elif option == 3:
        mark_done()
    elif option == 4:
        delete_task()
    elif option == 5:
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("⚠ Invalid choice. Try again!")
