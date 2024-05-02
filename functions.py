def get_todo(filePath = "todo.txt"):
    with open(filePath, 'r') as fileLocal:
        todo_local = fileLocal.readlines()
    return todo_local
def write_todo(todo_input ,filePath= "todo.txt"):
    with open(filePath, "w") as fileLocal:
        fileLocal.writelines(todo_input)
