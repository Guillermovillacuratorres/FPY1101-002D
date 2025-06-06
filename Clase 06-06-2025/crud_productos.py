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
while True:
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Editar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        id_producto = int(input("Ingrese el id del producto: "))
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
        for i in productos["productos"]:
            if i["id_producto"] == id_producto:
                nombre = input("Ingrese el nombre del producto: ")
                precio = int(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                i["nombre"] = nombre
                i["precio"] = precio
                i["cantidad"] = cantidad
                print("Producto agregado exitosamente!!!!")

    elif opcion == 4:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in productos["productos"]:
            if i["id_producto"] == id_producto:
                productos["productos"].remove(i)
                print("Producto eliminado correctamente!")

    elif opcion == 5:
        break
    else:
        print("Opcion no valida!!!")

#print(productos["productos"])