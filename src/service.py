import valiadation

task = []

def add_task():
    title = input("Enter the TASK name: ")
    description = input("Enter the TASK description: ")
    priority = input("Enter the TASK priority (high, mid, low)")

    print("\nSelect the Task status :")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    status_option = input("Enter an option: ")

    match status_option:
        case "1":
            status = 'Pending'
        case "2": 
            status = 'In Progress'
        case "3": 
            status = 'Completed'
        case _:
            print("error")
            status = 'Pending'
    if valiadation.validate_title(title) and valiadation.validate_description(description) and valiadation.validate_priority(priority):
        tasks ={
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        } 
        task.append(tasks)
    else:
        print("error")


def filter_tasks_by_status(tasks, search_status):
    """
    Filters tasks based on the provided status.
    
    Parameters:
        tasks (list): list of tasks (dictionaries)
        search_status (str): status to filter by
    
    Returns:
        list: list of tasks that match the status
    """
    if not tasks:
        return []

    search_status = search_status.strip().lower()

    filtered_tasks = [
        task for task in tasks
        if task.get("status", "").strip().lower() == search_status
    ]

    return filtered_tasks

task = []
def task_listing():
    option = -1
    if option == 3:
        print("the task list is: \n")
    if len(task) > 0:
        for i, j in enumerate(task, start=1):
            print(f'task #{i} . NAME:{j["title"]} STATE: {j["status"]} PRIORITY: {j["priority"]} \n')
    else:
        print("empty list")


def update_task():
    if task:
        task_listing()
        try:
            indice = int(input("Enter the task # to update: ")) - 1
            if 0 <= indice < len(task):
                task = task[indice]
                print("\nEnter the new task information (leave blank to stop making changes): ")
                title = input(f"Title ({task['title']}): ")
                description = input(f"Description ({task['description']}): ")
                priority = input(f"Priority ({task['priority']}): ")
                
                print("\nSelecct the task's new status: ")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")
                status_option = input("Enter the new task status (leave blank to stop making changes): ")

                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if priority:
                    if valiadation.validar_prioridad(priority):
                        task['priority'] = priority
                    else:
                        print("Invalid priority. Not changed.")
                if status_option:
                    match status_option:
                        case "1":
                            task['status'] = "pending"
                        case "2":
                            task['status'] = "in progress"
                        case "3":
                            task['status'] = "completed"
                        case _:
                            print("Invalid option. Not changed.")
                print("Task successfuly updated!")
            else:
                print("Invalid Index.")
        except ValueError:
            print("Invalid Index.")
    else:
        print("No tasks.")


def show_task(): #crea la funcion para mostrar tareas
    for i, t in enumerate(task): # utilizamos "for" "in" para que recorra todas las tareas teniendo en cuenta la posicion de la tarea (i), 0,1,2 y cada tarea "t" tittle
        print(i + 1, "-", t["title"]) #mostramos el resultado "print", el numero de la tarea "i", el guion "-" es solo para que se vea mas ordenado, "t" es titulo de la tarea, metemos en [] oara que muestre el nombre de la tarea seleccionada

def delete_task(): #Aqui creamos la funcion con "DEF"
    show_task() #Le mostramos al usuario las tareas para que el usuario vea cual va a borrar

    while True: #Usamos while true hasta que el usuario lo haga bien
        try:  #Intentamos utilizar el codigo sin que se rompa
            i = int(input("\nNumber to delete: ")) -1 #Pedimos un numero y lo convertimos a numero entero

            if i >= 0 and i < len(task): #Utilizamos len para que represente todos los elementos de una lista en este caso son 3
                task.pop(i) #PARA ELIMINAR LA TAREA UTILIZAMOS LA VARIABLE .pop()
                print("Task deleted\n") #Confirmamos al usuario la tarea confirmada, la /n significa que baje una linea
                break #Salimos del ciclo porque todo se ejecuto correctamente
            else:
                print("Invalid number") #Si el numero no exite = error

        except:
            print("Error, Enter a number\n") #Si el usuario escribe letras evita que se dañe todo el programa

            #RESUMEN: El usuario elige un numero, el programa valida que exista y luego elimina esa tarea usando .pop()
delete_task() #De la linea 29-32 es prueba

print("Final list:\n")
show_task ()
print()
