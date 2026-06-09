nombre = ""
#Sin argumentos - Sin retorno
def sumar():#---> no tiene parametros
    """Esta funcion es sin parametros y sin retorno, solo muestra la suma de 10 + 10."""
    nombre = "pedro"
    print(10 +10)


sumar() #--> no tiene argumentos


def restar()-> int:
    "Esta funcion es sin parametros pero con retorno, devuelve la resta de 100 - 70."
    return 100 - 70



resta = restar()
print(restar())




def multiplicar(n1:int,n2:int):
    "Esta funcion es sin retorno pero con parametros, muestra el resultado de la multiplicacion entre dos numeros."
    print(n1 * n2)

multiplicar(90,5)





def division(n1:int,n2:int)-> float:
    "Esta funcion es con parametros y con retorno, devuelve la divios entre dos numeros."
    return n1 / n2


print(division(500,5))