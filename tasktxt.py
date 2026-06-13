FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_task(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print("Error saving tasks:",e) 

def create_task(tasks):
    task = input("Enter new task:")
    tasks.append(task)
    save_task(tasks)
    print("Task added successfully")

def view_task(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n----Task List----")
    for index,task in enumerate(tasks,start=1):
        print(f"{index}.{task}")

def update_task(tasks):
    view_task(tasks)

    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to update:")) 

        if 1 <= task_num <= len(tasks):
            new_task = input("Enter new task:")
            tasks[task_num -1] = new_task 
            save_task(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_task(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_task(tasks)
            print(f"'{removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


tasks = load_tasks()

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_task(tasks)

    elif choice == "2":
        view_task(tasks)

    elif choice == "3":
        update_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("👋 Exiting Task Manager...")
        break

    else:
        print("❌ Invalid choice. Try again.")        

                      


                       