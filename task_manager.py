class Task:
    def __init__(self,title):
        self.title = title

    def __str__(self):
        return self.title


tasks = []

def create_task():
    title = input("Enter task title:")
    task = Task(title)
    tasks.append(task)
    print("Task added succesfully!")

def read_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    for index,task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def update_task():
    read_tasks()

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to update:"))

        if 1 <= task_num <= len(tasks):
            new_title = input("Enter new task title:")
            tasks[task_num - 1].title = new_title
            print("Task updated successfully!")
        else:
            print("Invalid task number:")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    read_tasks()

    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete:"))

        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f" '{removed_task}' deleted successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n----Task Manager----")
    print("1.Create Task")
    print("2.View Tasks")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")

    choice = input("Choose an option:") 

    if choice == '1':
        create_task()

    elif choice == '2':
        read_tasks()

    elif choice == '3':
        update_task()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        print("Exiting Task Manager...") 
        break

    else:
        print("Invalid choice. Please try again.")           


                    


                

                    
