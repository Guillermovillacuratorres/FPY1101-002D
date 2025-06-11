def valida_numero_entero_positivo(mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero < 0:
                print("Solo se permiten numero positivos.")
                continue
        except ValueError:
            print("Solo se permiten numeros enteros.")
            continue
        return numero
    
#edad = valida_numero_entero_positivo("Ingrese su edad: ")
#id_producto = valida_numero_entero_positivo("Ingrese el id del producto: ")

#print(f"edad {edad} - id {id_producto}")




def valida_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            print("El texto no puede estar vacio")
        elif len(texto) > 1:
            print("El texto no puede contener mas de un caracter.")
        else:
            return texto
           
#opcion = valida_texto("Ingrese A o B o C: ")

"""nombre = "Pedrito"
def test():
    nombre = "Juan"
    print("FUNC",nombre)

test()
print(nombre)
"""