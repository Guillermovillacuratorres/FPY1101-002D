mi_primera_lista = [1,2,9,81,7,47,8,3,1]

#Agregar elementos a una lista
mi_primera_lista.append("hola")

mi_primera_lista.insert(2,100)


#Eliminar un elemento de la lista
mi_primera_lista.remove("hola")

#mi_primera_lista.pop(20)

#Largo de la lista
#print(len(mi_primera_lista))


print(mi_primera_lista[1])


#print(mi_primera_lista)
contador = 0
for i in mi_primera_lista:
    if i == 1:
        mi_primera_lista.pop(contador)
        mi_primera_lista.insert(contador,99)
        
    contador += 1

mi_primera_lista.sort()
mi_primera_lista.reverse()
print(mi_primera_lista)