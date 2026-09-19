# ==========================================
#          TO-DO LIST - PROJECT 1
# ==========================================

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)
            print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        print("\n========== YOUR TASKS ==========")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Exit
    elif choice == "3":
        print("\nThank you for using the To-Do List!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")