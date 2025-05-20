while True:
    print("**** M E N U ****")
    print("[1] - Opción 1")
    print("[2] - Opción 2")
    print("[3] - Opción 3")
    print("[4] - Opción 4")
    try:
        opcion = int(input("Seleccione una opción:"))
    except:
        print("Error, debe ingresar numeros enteros.")

    if opcion == 1:
        print("Opcion 1")
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
        break
    else:
        print("Opcion no valida!")


