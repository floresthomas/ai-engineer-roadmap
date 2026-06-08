def get_status(done):
    if done:
        return "Done"

    return "Pending"


def print_tasks(tasks):
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


tasks = [
    {"title": "Learn Python", "done": True},
    {"title": "Practice English", "done": False},
]

title = input("Enter task title: ")
answer = input("Is it done? yes/no: ")

done = answer.lower() == "yes"

add_task(tasks, title, done)

print_tasks(tasks)