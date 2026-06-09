import json


def load_tasks():
    try:
        with open("tasks.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def get_status(done):
    if done:
        return "Done"

    return "Pending"


def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("Today's tasks:")

    for index, task in enumerate(tasks, start=1):
        status = get_status(task["done"])
        print(f"{index}. {task['title']} - {status}")


def add_task(tasks, title, done):
    new_task = {
        "title": title,
        "done": done
    }

    tasks.append(new_task)

def mark_task_as_done(tasks, task_number):
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)

    print("Task marked as done.")

def delete_task(tasks, task_number):
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks.pop(index)
    save_tasks(tasks)

    print("Task deleted succesfully")

def show_menu():
    print()
    print("Task Manager")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete Task")
    print("5. Exit")


tasks = load_tasks()

while True:
    show_menu()

    option = input("Choose an option: ")

    if option == "1":
        print_tasks(tasks)

    elif option == "2":
        title = input("Enter task title: ")
        answer = input("Is it done? yes/no: ")

        done = answer.lower() == "yes"

        add_task(tasks, title, done)
        save_tasks(tasks)

        print("Task added successfully.")

    elif option == "3":
        task_number = int(input("Enter task number: "))
        mark_task_as_done(tasks, task_number)
        
    elif option == "4":
        task_number = int(input("Enter task number: "))
        delete_task(tasks, task_number)

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")