while True:
    try:
        numero_uno = int(input("Ingrese el primer número:"))
        if numero_uno <= 0:
            print("Error, solo se permiten números positivos o mayores a cero.")
            continue
        numero_dos = int(input("Ingrese el segundo número:"))
        if numero_dos <= 0:
            print("Error, solo se permiten números positivos o mayores a cero.")
            continue
    except ValueError:
        print("Solo se permiten valores numericos enteros.")
        continue
    else:
        break


while True:
    print("------ M E N Ú ------")
    print("[1] - Sumar")
    print("[2] - Restar")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    print("[5] - Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("La opción debe ser un numero entero.")
        continue

    if opcion == 1:
        print("La suma de los dos números es ", numero_uno + numero_dos)
    elif opcion == 2:
            print("La resta de los dos números es ", numero_uno - numero_dos)
    elif opcion == 3:
        print("La multiplicación de los dos números es ", numero_uno * numero_dos)
    elif opcion == 4:
        print("La división de los dos números es ", numero_uno / numero_dos)
    elif opcion == 5:
        print("Saliendo!!!!")
        break
    else:
        print("Opcion no valida, ingrese una opcion del 1 al 5.")

