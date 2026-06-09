def validar_enteros_positivos(msg:str):
    while True:
        try:
            valor = int(input(msg))
            if valor == 0:
                print("EL valor no puede ser cero.")
            elif valor < 0:
                print("El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Solo se permiten numeros enteros.")

def sumar(n1,n2):
    return n1 + n2


while True:
    print("[1] Sumar")
    print("[2] Restas")
    print("[3] Dividir")
    print("[4] Multiplicar")
    print("[5] Salir")
    opcion = validar_enteros_positivos("Ingrese una opcion: ")
    if opcion == 1:
        n1 = validar_enteros_positivos("Ingrese el primer numero: ")
        n2 = validar_enteros_positivos("Ingrese el segundo numero: ")
        print("La suma de los dos numeros es: ", sumar(n1,n2))
