#Sin argumentos - sin retorno
def sumar():
    """Esta funcion muestra un mensaje que dice hola"""
    print("Hooola")

#sumar()

#Con argumentos - sin retorno
def sumar(n1:int,n2:int,nombre:str=""):
    print("N1 ", n1)
    print("N2 ", n2)
    print(n1 + n2)
    print(nombre)


#sumar(n2=40,n1=60,nombre="Juan")

#Sin argumentos - con retorno
def multiplicar()->str:
    return 9*10

#print(multiplicar())
resultado_multiplicacion = multiplicar()
#print(resultado_multiplicacion)

#Con argumentos - con retorno
def multiplicacion(n1:int,n2:int) -> int:
    return n1*n2

print(multiplicacion(5,5))