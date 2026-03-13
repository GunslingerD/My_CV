
entrada = True
salida = False

class Inventario:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad



    def actualizar_inventario(self, producto, cantidad, accion):

        if accion == True :
            self.cantidad += cantidad

inventario = Inventario("Vasos", 5)


print(inventario.cantidad)
inventario.actualizar_inventario("Latas", 5, entrada)
print(inventario.cantidad)  