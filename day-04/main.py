import json

tasks_list = [
    {"title": "Learn Python", "done": True},
    {"title": "Practice English", "done": False},
    {"title": "Build AI Project", "done": False}
]

def save_tasks(tasks):
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file)

def load_tasks():
    with open('tasks.json', 'r') as json_file:
        data = json.load(json_file)

    return data

def print_tasks(tasks):
    with open('tasks.json', 'r') as json_file:
        data = json.load(json_file)

    print(data)

save_tasks(tasks_list)

loaded_tasks = load_tasks()

print_tasks(loaded_tasks)