listados_de_juegos = []

def validar_numero_entero_positivo(msg:str):
    while True:
        try:
            valor = int(input(msg))
            if valor == 0:
                print("El valor no puede ser 0")
            elif valor < 0:
                print("El valor no puede ser menor a 0")
            else:
                return valor
        except:
            print("El valor solo puede ser numerico")

def valida_string(msg:str)->str:
    while True:
            valor = input(msg)
            if len(valor)<3:
                print("el valor no puede contener menos de 3 letras")
            elif valor.isalpha() == False: 
                print ("solo se permiten letras")
            else:
                return valor
            

def buscar_juego(id_juego:int) -> int | None:
    contador = 0
    encontrado = False
    for i in listados_de_juegos:

        if i["id_juego"] == id_juego:
            #encontrado = True
            return contador
        contador += 1


def agregar_juego(id_juego:int,nombre_juego:str,genero_juego:str,precio_juego:int,cantidad_juego:int):
    diccionario = {
        "id_juego":id_juego,
        "nombre_juego":nombre_juego,
        "genero_juego":genero_juego,
        "precio_juego":precio_juego,
        "cantidad_juego":cantidad_juego,
    }
    listados_de_juegos.append(diccionario)

def menu():
    while True:
        print("1 - Agregar juego")
        print("2 - Mostrar juegos")
        print("3 - Eliminar juego")
        print("4 - Actualizar juego")
        print("5 - Salir")

        
        opc = validar_numero_entero_positivo("Ingrese una opcion entre el 1 y 5: ")
        if opc != 1 and opc !=2 and opc!=3 and opc!= 4 and opc!=5:
            print("Ingrese una opcion valida (1-2-3-4-5).")
        if opc == 1:
            id_juego= validar_numero_entero_positivo("Ingrese el id del juego: ")
            nombre_juego = valida_string("Ingrese el nombre del juego: ")
            genero_juego = valida_string("Ingrese el genero del juego: ")
            precio_juego = validar_numero_entero_positivo("Ingrese  el precio del juego: ")
            cantidad_juego = validar_numero_entero_positivo("Ingrese la cantidad del juego: ") 
            agregar_juego(id_juego,nombre_juego,genero_juego,precio_juego,cantidad_juego)
            print("Juego agregado")
        if opc == 2:
            #print(listados_de_juegos)
            print(buscar_juego(1))
menu() 



