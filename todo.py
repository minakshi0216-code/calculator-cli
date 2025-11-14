#To do list application
#created by Minakshi
tasks = []   

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No tasks added ")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def delete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye")
        break
    else:

        print("Invalid choice")
