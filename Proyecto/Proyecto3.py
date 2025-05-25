tareas = [
    {"nombre": "Estudiar Python", "prioridad": "Alta"},
    {"nombre": "Hacer ejercicio", "prioridad": "Media"},
    {"nombre": "Leer un libro", "prioridad": "Baja"}
]

prioridades = ["Alta", "Media", "Baja"]
while True:
    print("======= GESTOR DE TAREAS =======")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Clasificar tarea")
    print("5. Salir")
    print("===============================")
    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea a agregar:")
        prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
        if prioridad in prioridades:
            tareas.append(tarea)
            print("Tarea agregada con éxito")
        else:
            print("Prioridad no válida")
        
    elif opcion == "2":
        print("Tareas pendientes:")
        for tarea in tareas:
            print(tarea)

    elif opcion == "3":
        tarea = input("Ingrese la tarea a eliminar: ")
    
        if tarea in tareas:
            tareas.remove(tarea)
            print("Tarea eliminada con éxito")
        else:
            print("Tarea no encontrada")
        
    elif opcion == "4":
        tarea = input("Ingrese la tarea a clasificar: ")
        prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
    
        if tarea in tareas:
            if prioridad in prioridades:
                tareas.remove(tarea)
                tareas.append(tarea)
                print("Tarea clasificada con éxito")
            else:
                print("Prioridad no válida")
        else:
            print("Tarea no encontrada")
        
    elif opcion == "5":
        print("Saliendo...")
        
    break
    
      