canciones=[]
def actualiza_cancion(id_cancion:int,nombre_cancion:str,artista_cancion:str,album_cancion:str,duracion_cancion:str):
        cancion_encontrada=buscar_cancion(id_cancion)
        print(cancion_encontrada)
        cancion=canciones[cancion_encontrada]
        cancion["nombre_cancion"]=nombre_cancion
        cancion["artista_cancion"]=artista_cancion
        cancion["album_cancion"]=album_cancion
        cancion["duracion_cancion"]=duracion_cancion
        print("Cancion actualizada.")
def mostrar_cancion():
    if len(canciones) == 0:
        print("no hay canciones registradas")
    else:
        for i in canciones:
            print(f"nombre: {i["nombre_cancion"]} - artista:{i["artista_cancion"]} - album:{i["album_cancion"]}")

def buscar_cancion(idcancion:int) -> int | None:
    contador = 0
    for i in canciones:
        if i["id_cancion"]==idcancion:
            return contador
        contador += 1
            

def validar_string(mensaje:str):
    while True:
        valor = input(mensaje)
        if len(mensaje) < 1:
            print("Inválido! EL largo del valor debe tener al menos 1 caracter")
        else:
            return valor

        
def agregar_cancion(idcancion:int,nombrecancion:str,artistacancion:str,albuncancion:str,duracioncancion:int):
    diccionario={
        "id_cancion" : idcancion,
        "nombre_cancion" : nombrecancion,
        "artista_cancion" : artistacancion,
        "album_cancion" : albuncancion,
        "duracion_cancion" : duracioncancion
    }
    canciones.append(diccionario)
    print("cancion agregada correctamente ")
    
def validar_enteros_positivos(mensaje:str):
    while(True):
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print("El valor debe ser mayor que 0")
            elif valor < 0:
                print("El valor debe ser un numero entero positivo")
            else:
                return valor
        except Exception as e:
            print("Solo se permiten numeros enteros")



def menu():
    while(True):
        print("----- Menu -----")
        print("")
        print("(1) - Agregar Cancion")
        print("(2) - Mostrar Canciones")
        print("(3) - Actualizar Canciones")
        print("(4) - Eliminar Cancion")
        print("(5) - Salir")

        opc = validar_enteros_positivos("Ingrese una opcion: ")

        if opc==1:
            id_cancion = validar_enteros_positivos("Ingrese un id de cancion: ")
            if buscar_cancion(id_cancion) == None:
                nombre_cancion = validar_string("Ingrese el nombre de la cancion: ")
                artista_cancion = validar_string("Ingrese el nombre del artista de la cancion: ")
                album_cancion = validar_string("Ingrese el nombre del album de la cancion: ")
                duracion_cancion = validar_enteros_positivos("Ingrese la duracion de la cancion: ")
                agregar_cancion(id_cancion, nombre_cancion, artista_cancion,album_cancion, duracion_cancion)
            else:
                print("El Id ya existe en el listado de cancion")
                continue
        elif opc==2:
            mostrar_cancion()
        elif opc ==3:
            id_cancion=validar_enteros_positivos("Ingrese el id de la cancion que desea actualiza: ")
            cancion_encontrada=buscar_cancion(id_cancion)
            if cancion_encontrada==None:
                print("La cancion no se encontro en la lista")
            else:
                nombrecancion=validar_string("Ingrese el nombre de la cancion: ")
                artistacancion=validar_string("Ingrse el nombre del artista de la cancion: ")
                albumcancion=validar_string("Ingresar el nombre del album de la cancion: ")
                duracioncancion=validar_enteros_positivos("Ingrese la duracion de la cancion: ")
                actualiza_cancion(cancion_encontrada,nombrecancion,artistacancion,albumcancion,duracioncancion)

menu()

