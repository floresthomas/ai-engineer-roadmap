def todoList():
    lista = ["Learn Python", "Practice English", "Build AI Project"]

    print("Today task´s: ")
    for index, task in enumerate(lista, start = 1):
        print(f"{index}. {task}")

todoList()