tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(task_number):
    try:
        del tasks[task_number - 1]
        print("Task removed successfully")
    except IndexError:
        print("Invalid task number")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter task number: "))
        remove_task(task_number)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
