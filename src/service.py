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
        case 1:
            status = 'Pending'
        case 2: 
            status = 'In Progress'
        case 3: 
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











listar_tareas= ""
def actualizar_tarea():
    if task:
        listar_tareas()
        try:
            indice = int(input("Ingrese el número de la tarea a actualizar: ")) - 1
            if 0 <= indice < len(task):
                tarea = task[indice]
                print("\nIngrese los nuevos datos de la tarea (dejar en blanco para no cambiar):")
                titulo = input(f"Título ({tarea['titulo']}): ")
                descripcion = input(f"Descripción ({tarea['descripcion']}): ")
                prioridad = input(f"Prioridad ({tarea['prioridad']}): ")
                
                print("\nSeleccione el nuevo estado de la tarea:")
                print("1. Pendiente")
                print("2. En progreso")
                print("3. Completada")
                opcion_estado = input("Ingrese una opción (dejar en blanco para no cambiar): ")

                if titulo:
                    tarea['titulo'] = titulo
                if descripcion:
                    tarea['descripcion'] = descripcion
                if prioridad:
                    if valiadation.validar_prioridad(prioridad):
                        tarea['prioridad'] = prioridad
                    else:
                        print("Prioridad inválida. No se cambió la prioridad.")
                if opcion_estado:
                    match opcion_estado:
                        case "1":
                            tarea['estado'] = "pendiente"
                        case "2":
                            tarea['estado'] = "en progreso"
                        case "3":
                            tarea['estado'] = "completada"
                        case _:
                            print("Opción inválida. No se cambió el estado.")
                print("Tarea actualizada con éxito!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Índice inválido.")
    else:
        print("No hay tareas.")
