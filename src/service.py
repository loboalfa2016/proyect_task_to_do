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


