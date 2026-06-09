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


def show_menu():
    print()
    print("Task Manager")
    print("1. List tasks")
    print("2. Add task")
    print("3. Exit")


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
        print("Goodbye!")
        break

    else:
        print("Invalid option.")