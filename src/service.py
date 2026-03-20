import valiadation

task = []

def add_task():
    titulo = input("ingrese el nombre de la tarea")
    descripcion = input(" ingrese la descripcionde la tarea")
    prioridad = input("ingrese la prioridad de la tarea(alta, media, baja)")

    print("\nSeleccione el estado de la tarea:")
    print("1. Pendiente")
    print("2. En progreso")
    print("3. Completada")
    opcion_estado = input("Ingrese una opción: ")

    match opcion_estado:
        case 1:
            estado = 'pendiente'
        case 2: 
            estado = 'en progreso'
        case 3: 
            estado = 'completado'
        case _:
            print("error")
            estado = 'pendiente'
    if valiadation.validar_titulo(titulo) and valiadation.validar_descripcion(descripcion) and valiadation.validar_prioridad(prioridad):
        tasks ={
            "titulo": titulo,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "estado": estado
        } 
        task.append(tasks)
    else:
        print("error")















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
