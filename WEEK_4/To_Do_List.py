# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Add a task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")

# Mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = f"[✔] {tasks[index]}"
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")

# Show menu
def show_menu():
    print("===== TO-DO LIST APP =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

# Main loop
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
