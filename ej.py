MOTOCICLETA = 500
AUTO = 1000
CAMION = 2500

contador_motocicleta = 0
contador_auto = 0
contador_camion = 0

acumulador_motocicleta = 0
acumulador_auto = 0
acumulador_camion = 0 

while True:
    print("[1] - Registrar Motocicleta ($500)")
    print("[2] - Registrar Auto ($1.000)")
    print("[3] - Registrar Camión ($2.500)")
    print("[4] - Salir y mostrar reporte.")

    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
            if opc < 1 or opc > 4:
                print("Las opciones son (1-2-3-4)")
            else:
                break
        except:
            print("Solo se permiten numeros.")

    if opc == 1:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de motos a registrar: "))
                if cantidad <= 0:
                    print("La cantidad de motos a registrar no debe ser cero o menor.")
                else:
                    break
            except:
                print("Solo se permiten numeros.")
        
        for i in range(cantidad):
            while True:
                patente = input("Ingrese la patente: ")

                if len(patente) <= 0:
                    print("La patente no debe estar vacia")
                elif len(patente) > 5:
                    print("La patenete no debe contener mas de 5 caracteres")
                elif len(patente) <= 4:
                    print("La patenete no debe contener menos de 5 caracteres")
                else:
                    break

            contador_motocicleta += 1
            acumulador_motocicleta += MOTOCICLETA


    if opc == 2:
        print("opcion 2")
    if opc == 3:
        print("opcion 3")
    if opc == 4:
        print(f"Pasaron {contador_motocicleta} motos con un total de ${acumulador_motocicleta}")
        total = acumulador_motocicleta + acumulador_auto + acumulador_camion
        print(f"Total recaudado ${total}")
        break
