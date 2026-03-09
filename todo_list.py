tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except:
    pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:
    print("\nTO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")

    elif choice == "3":
        task = input("Enter task to delete: ")
        if task in tasks:
            tasks.remove(task)
            save_tasks()
            print("Task removed.")
        else:
            print("Task not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")