
entrada = True
salida = False

class Inventario:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad



    def actualizar_inventario(self, producto, cantidad, accion):

        if accion == 1 :
            self.cantidad += cantidad

Nuevo_producto = Inventario("Latas", 5)

print(Nuevo_producto.cantidad)
Nuevo_producto.actualizar_inventario("Latas", 5, entrada)
print(Nuevo_producto.cantidad)