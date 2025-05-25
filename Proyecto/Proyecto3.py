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
            tareas.append({"nombre": tarea, "prioridad": prioridad})
            print("Tarea agregada con éxito")
        else:
            print("Prioridad no válida")
        
    elif opcion == "2":
        print("Tareas pendientes:")
        for t in tareas:
            print(f"{t['nombre']} - Prioridad: {t['prioridad']}")

    elif opcion == "3":
        tarea = input("Ingrese la tarea a eliminar: ")
        encontrada = False
        for t in tareas:
            if t["nombre"] == tarea:
                tareas.remove(t)
                encontrada = True
                print("Tarea eliminada con éxito")
                break
        if not encontrada:
            print("Tarea no encontrada")
        
    elif opcion == "4":
        tarea = input("Ingrese la tarea a clasificar: ")
        prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
        encontrada = False
        for t in tareas:
            if t["nombre"] == tarea:
                if prioridad in prioridades:
                    t["prioridad"] = prioridad
                    print("Tarea clasificada con éxito")
                else:
                    print("Prioridad no válida")
                encontrada = True
                break
        if not encontrada:
            print("Tarea no encontrada")
        
    elif opcion == "5":
            print("Saliendo...")
            break
    else:
        print("Opción no válida")
    
      