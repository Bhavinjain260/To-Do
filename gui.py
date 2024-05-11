import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text(" Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
refreshButton = sg.Button("Refresh")
completeButton = sg.Button("complete", key= "complete")
exitButton = sg.Button("Exit", key= "exit")

list_box = sg.Listbox(values= functions.get_todo(),
                      key="todos",
                      enable_events= True,

                      size= [45,10])

edit_button = sg.Button("Edit")
layout = [[clock],[label], [input_box, add_button, refreshButton], [list_box, edit_button, completeButton], [exitButton]]




window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=190)


    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    else:
        window["clock"].update(value=time.strftime("%b %d, %Y %H:%S"))

    match event:
        case "Add":
            todos = functions.get_todo()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)

            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value = values["todos"][0])

        case "complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todo()
                todos.remove(todo_to_remove)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Refresh":
            todos = functions.get_todo()
            window["todos"].update(values=todos)

        case "todos":
             window["todo"].update(value=values["todos"][0])
        case "exit":
            break
        case sg.WIN_CLOSED:
            break





window.close()