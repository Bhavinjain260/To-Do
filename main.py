from functions import get_todo, write_todo

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.title()
        todos = get_todo()
        todos.append(todo + "\n")
        write_todo(todos)

    elif user_action.startswith("show"):

        todos = get_todo()
        new_list = []
        for index, new_list in enumerate(todos, 1):
            new_list = new_list.strip("\n")
            print(f"{index}. {new_list}")

    elif user_action.startswith("edit"):

        try:
            edit_todo_number = int(user_action[5:])
            edit_todo_number = edit_todo_number - 1
        
            new_todo = input("Enter a New Todo: ")
            todos = get_todo()
            todos[edit_todo_number ] = new_todo + " " +  "\n"
            write_todo(todos)

        except ValueError:
            print("There is no Item with that number in the list.")
            continue


    elif user_action.startswith("complete"):
        try:
            completed_Todo_num = int(user_action[9:])
            print("The selected Todo has been marked as completed.")
            todos = get_todo()
            index = completed_Todo_num - 1
            to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todo( todos)

        except IndexError:
            print("Please enter a valid Todo number.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command.")

print("Bye")
