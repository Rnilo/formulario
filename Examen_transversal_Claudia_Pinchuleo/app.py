import utilidades

while True:
    print("\nMenú:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        utilidades.asignar_sueldos()
    elif opcion == "2":
        utilidades.clasificar_sueldos()
    elif opcion == "3":
        utilidades.ver_estadisticas()
    elif opcion == "4":
        utilidades.reporte_sueldos()
    elif opcion == "5":
        print("Finalizando programa...")
        print("Desarrollado por Claudia Pinchuleo")
        print("RUT 17.839.756-7")
        break
    else:
        print("Opción no válida, por favor seleccione nuevamente.")
