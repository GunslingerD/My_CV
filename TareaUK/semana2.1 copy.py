#Declaramos el diccionario por el momento vacio.
inventario = {}

#Declaramos los valores de las variables para el parametro accion en la siguiente funcion.
entrada = True
salida = False

#Definimos la funcion actualizar_inventario() con los parametros producto, cantidad, accion.
def actualizar_inventario(producto, cantidad, accion):
    #En caso de que la accion sea entrada y:
    if accion == entrada:
      #Si el producto existe en inventario se suma cantidad a la cantidad ya existente.
      if producto in inventario: 
        inventario[producto] += cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}pzs")
      #Si el producto no existe en inventario, se agrega al diccionario y se agrega la cantidad igualmente.
      else:
        inventario[producto] = cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}pzs")
    #Si la accion es salida y:
    elif accion == salida:
      #Si el producto esta en inventario y la cantidad ingresada a la funcion es menor o igual a la que hay en inventario, se resta dicha cantidad.
      if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print("////////////////////////")
        print(f"Inventario actualizado: \nProducto: {producto} \nCantidad: {inventario[producto]}pzs")
      #Si la cantidad ingresada es mayor a la que hay en inventario, devuelve un mensaje de error.
      elif producto in inventario and inventario[producto] < cantidad:
        print("////////////////////////")
        print("Error :/ \nCantidad de salida mayor al stock")
      #En el caso de que el producto no este en inventario, devuelve un mensaje de error.
      else:
        print("////////////////////////")
        print("Error :/ \nProducto no existente en el inventario")


#Escenario 1: Añadimos un producto que no estaba en la lista con su respectiva cantidad.
actualizar_inventario("Vasos", 5, True)

#Escenario 2: Se agrega una cantidad de un producto ya existente en el inventario.
actualizar_inventario("Vasos", 6, entrada)

#Escenario 3: Se resta una cantidad de un producto ya existente en el inventario.
actualizar_inventario("Vasos", 13, salida)

#Escenario 3: Se resta una cantidad de un producto no existente en el inventario.
actualizar_inventario("Tenedores", 13, salida)

def reporte_inventario():
  print("////////////////////////")
  print("Inventario final:")
  for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}pzs")

reporte_inventario()

transacciones = [
  ("Cucharas:",5, entrada),
  ("Cuchillos:",6, entrada),
  ("Ollas:",2, entrada),
  ("Termos:",3, entrada),
]

for transaccion in transacciones:
  producto, cantidad, accion = transaccion
  actualizar_inventario(producto, cantidad, accion)

actualizar_inventario("Tazos", 5, salida)