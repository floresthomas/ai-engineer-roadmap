def tasks_lists():
    tasks = [
        {"title": "Learn Python", "done": True},
        {"title": "Practice English", "done": True},
        {"title": "Build AI Project", "done": False}
    ]

    for task in tasks:
        print(task["title"], task["done"])

tasks_lists()