#Declaramos el diccionario por el momento vacio.
inventario = {}

#Declaramos los valores de las variables para el parametro accion en la siguiente funcion.
entrada = True
salida = False

#Definimos la funcion actualizar_inventario() con los parametros producto, cantidad, accion.
def actualizar_inventario(producto, cantidad, accion):
    if accion == entrada:
      if producto in inventario:
        inventario[producto] += cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}")
      else:
        inventario[producto] = cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}")
    elif accion == salida:
      if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}")
      elif producto in inventario and inventario[producto] < cantidad:
        print("**Error, cantidad de salida mayor al stock")


#Escenario 1: Añadimos un producto que no estaba en la lista con su respectiva cantidad.
actualizar_inventario("Vasos", 5, True)

#Escenario 2: Se agrega una cantidad de un producto ya existente.
actualizar_inventario("Vasos", 6, entrada)

#Escenario 2: Se agrega una cantidad de un producto ya existente.
actualizar_inventario("Tenedores", 6, entrada)

actualizar_inventario("Vasos", 11, salida)

actualizar_inventario("Vasos", 5, entrada)

