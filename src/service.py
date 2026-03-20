task = [    #DE LA LINEA 1 a 5 es para probar
    {"title": "Study"},
    {"title": "Go to gym"},
    {"title": "Sleep"}
]

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
