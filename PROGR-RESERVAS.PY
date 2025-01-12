# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad_stock):
        """
        Constructor de la clase Producto. Inicializa los atributos del producto.
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param cantidad_stock: Cantidad de producto disponible en el inventario.
        """
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad_stock = cantidad_stock  # Cantidad disponible en el inventario

    def actualizar_stock(self, cantidad_vendida):
        """
        Actualiza el stock del producto después de realizar una venta.
        :param cantidad_vendida: Cantidad de producto vendida.
        """
        if cantidad_vendida <= self.cantidad_stock:
            self.cantidad_stock -= cantidad_vendida
            print(f"{cantidad_vendida} unidades de {self.nombre} vendidas.")
        else:
            print(f"No hay suficiente stock para vender {cantidad_vendida} unidades de {self.nombre}.")

    def aplicar_descuento(self, porcentaje_descuento):
        """
        Aplica un descuento al precio del producto.
        :param porcentaje_descuento: Descuento en porcentaje que se aplicará al precio del producto.
        :return: Nuevo precio con el descuento aplicado.
        """
        descuento = self.precio * (porcentaje_descuento / 100)
        nuevo_precio = self.precio - descuento
        print(f"Nuevo precio de {self.nombre} con {porcentaje_descuento}% de descuento: {nuevo_precio:.2f}")
        return nuevo_precio


# Clase Cliente
class Cliente:
    def __init__(self, nombre, saldo):
        """
        Constructor de la clase Cliente. Inicializa los atributos del cliente.
        :param nombre: Nombre del cliente.
        :param saldo: Cantidad de dinero disponible para gastar.
        """
        self.nombre = nombre  # Nombre del cliente
        self.saldo = saldo  # Dinero disponible para gastar

    def realizar_compra(self, producto, cantidad):
        """
        Realiza una compra de un producto si el cliente tiene suficiente saldo.
        :param producto: El producto que se desea comprar.
        :param cantidad: La cantidad de producto que se desea comprar.
        """
        total_precio = producto.precio * cantidad
        if self.saldo >= total_precio:
            producto.actualizar_stock(cantidad)  # Actualiza el stock del producto
            self.saldo -= total_precio  # Reduce el saldo del cliente
            print(f"{self.nombre} ha comprado {cantidad} unidad(es) de {producto.nombre} por {total_precio:.2f}.")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para realizar esta compra.")

    def aplicar_descuento(self, producto, porcentaje_descuento):
        """
        Aplica un descuento a un producto al momento de la compra si el cliente lo desea.
        :param producto: El producto al que se le aplicará el descuento.
        :param porcentaje_descuento: El porcentaje de descuento a aplicar.
        """
        nuevo_precio = producto.aplicar_descuento(porcentaje_descuento)
        self.realizar_compra(producto, 1)  # Realiza la compra de una unidad con descuento
        print(f"{self.nombre} ha aplicado un descuento y ha pagado {nuevo_precio:.2f} por {producto.nombre}.")


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        """
        Constructor de la clase Tienda. Inicializa el nombre de la tienda y una lista vacía de productos.
        :param nombre: Nombre de la tienda.
        """
        self.nombre = nombre  # Nombre de la tienda
        self.productos = []  # Lista de productos en la tienda

    def agregar_producto(self, producto):
        """
        Agrega un producto a la tienda.
        :param producto: Producto a agregar a la tienda.
        """
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda {self.nombre}.")

    def mostrar_productos(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        print(f"\nProductos disponibles en la tienda {self.nombre}:")
        for producto in self.productos:
            print(f"{producto.nombre} - {producto.precio:.2f} (Stock: {producto.cantidad_stock})")


# Crear objetos de las clases
tienda = Tienda("La Tienda de Juan")
producto1 = Producto("Camiseta", 15.50, 100)
producto2 = Producto("Pantalón", 25.00, 50)
producto3 = Producto("Zapatos", 40.00, 30)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Mostrar productos disponibles
tienda.mostrar_productos()

# Crear cliente
cliente1 = Cliente("Carlos", 100.00)

# Cliente compra productos
cliente1.realizar_compra(producto1, 2)  # Compra 2 camisetas

# Aplicar descuento y realizar compra
cliente1.aplicar_descuento(producto2, 10)  # Aplica un 10% de descuento a un pantalón

# Mostrar saldo final del cliente
print(f"\nSaldo restante de {cliente1.nombre}: {cliente1.saldo:.2f}")
