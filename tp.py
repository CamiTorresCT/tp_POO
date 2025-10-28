class Carrito:

def _init_(self, usuario="Cliente"):

    self.productos = []         # lista de productos

    self.__total = 0.0          # atributo encapsulado (no accesible directamente)

    self.usuario = usuario      # tercer atributo requerido



def agregar_producto(self, nombre, precio):

    if not nombre or nombre.strip() == "":

        print("El nombre del producto no puede estar vacío.")

        return

    if precio <= 0:

        print("El precio debe ser mayor que 0.")

        return

    self.productos.append({"nombre": nombre.strip(), "precio": precio})

    self.__total += precio

    print(f"Producto '{nombre.strip()}' agregado. Precio: ${precio:.2f}")



def eliminar_producto(self, nombre):

    if not nombre or nombre.strip() == "":

        print("Ingrese un nombre válido.")

        return

    nombre = nombre.strip().lower()

    for p in self.productos:

        if p["nombre"].lower() == nombre:

            self.productos.remove(p)

            self.__total -= p["precio"]

            print(f"Producto '{p['nombre']}' eliminado.")

            return

    print("No se encontró ese producto en el carrito.")



def mostrar_carrito(self):

    if not self.productos:

        print(f"Carrito de {self.usuario} vacío.")

        return

    print(f"\nProductos en el carrito de {self.usuario}:")

    for i, p in enumerate(self.productos, 1):

        print(f"{i}. {p['nombre']} - ${p['precio']:.2f}")

    print(f"Total: ${self.__total:.2f}\n")



def consultar_total(self):

    return self.__total

Menú simple (3-5 opciones)

def menu():

usuario = input("Nombre de usuario (opcional): ").strip() or "Cliente"

carrito = Carrito(usuario)



while True:

    print("\n===== MENÚ =====")

    print("1. Agregar producto")

    print("2. Eliminar producto")

    print("3. Mostrar carrito")

    print("4. Consultar total")

    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()



    if opcion == "1":

        nombre = input("Nombre del producto: ")

        try:

            precio = float(input("Precio: "))

        except ValueError:

            print("Precio inválido. Ingrese un número.")

            continue

        carrito.agregar_producto(nombre, precio)



    elif opcion == "2":

        nombre = input("Nombre del producto a eliminar: ")

        carrito.eliminar_producto(nombre)



    elif opcion == "3":

        carrito.mostrar_carrito()



    elif opcion == "4":

        total = carrito.consultar_total()

        print(f"Total actual: ${total:.2f}")



    elif opcion == "5":

        print("Gracias. Saliendo.")

        break



    else:

        print("Opción inválida. Intente nuevamente.")

if name == "main":

menu()