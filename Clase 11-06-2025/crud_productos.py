import validacion
productos = {
    "productos":
    [
        {
            "id_producto": 1,
            "nombre":"Audifonos",
            "cantidad":10,
            "precio":590
        },
        {
            "id_producto": 2,
            "nombre":"Mouse",
            "cantidad":50,
            "precio":600
        }
    ]
}


def buscar_producto(id_producto:int):
    for i in productos["productos"]:
        if i["id_producto"] == id_producto:
            return i





while True:
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Editar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        #id_producto = int(input("Ingrese el id del producto: "))
        id_producto = validacion.valida_numero_entero_positivo("Ingrese el id del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        producto_agregar = {
            "id_producto": id_producto,
            "nombre":nombre,
            "cantidad":cantidad,
            "precio":precio
        }
        productos["productos"].append(producto_agregar)
        print("Producto agregado correctamente!!!")
    
    elif opcion == 2:
        for i in productos["productos"]:
            print(f"NOMBRE: {i["nombre"]} PRECIO: {i["precio"]} CANTIDAD: {i["cantidad"]}")

    elif opcion == 3:
        id_producto = int(input("Ingrese el id del producto: "))
        producto_encontrado = buscar_producto(id_producto)
        print(producto_encontrado)
        if producto_encontrado == None:
            print("Producto no encontrado")
            continue

        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto_encontrado["nombre"] = nombre
        producto_encontrado["precio"] = precio
        producto_encontrado["cantidad"] = cantidad
        print("Producto agregado exitosamente!!!!")

    elif opcion == 4:
        id_producto = int(input("Ingrese el id del producto: "))
        producto_encontrado = buscar_producto(id_producto)
        productos["productos"].remove(producto_encontrado)
        print("Producto eliminado correctamente!")

    elif opcion == 5:
        break
    else:
        print("Opcion no valida!!!")

#print(productos["productos"])