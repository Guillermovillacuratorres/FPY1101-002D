diccionario = {
    "nombre":"Pedrito",
    "color":["rojo","verde"],
    "direccion":"mi casa",
    "hermanos":{
        "nombre":"Juan",
        "color":"verde",
        "edad":15
    }
}

diccionario2 = dict(nombre = "Juanito")

#print(diccionario["nombre"])

print(diccionario.get("nombre"))
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())


for clave, valor in diccionario.items():
    print(f"CLAVE: {clave} - VALOR: {valor}")