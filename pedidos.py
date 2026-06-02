from clientes import clientes
from utilidades import pedir_numero

# --- CONSTANTES ---
IVA = 0.21
DESCUENTO_GRANDE = 0.15
DESCUENTO_PEQUENO = 0.05
UMBRAL_GRANDE = 100
UMBRAL_PEQUENO = 50

pedidos = []

def menu_pedidos():
    """
    Muestra el menú principal de gestión de pedidos.
    Permite al usuario navegar entre las opciones de crear, listar y calcular totales.
    """
    fin = False
    while fin == False:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    """
    Inicia el flujo para registrar un nuevo pedido en el sistema.
    Asocia el pedido a un cliente existente y permite añadir múltiples líneas de productos.
    """
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    i = 0
    while i < len(clientes):
        print(str(i + 1) + ". " + clientes[i]["nombre"])
        i = i + 1

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append({"producto": producto, "cantidad": cantidad, "precio": precio})
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {"cliente": clientes[numero_cliente - 1], "lineas": lineas, "estado": "pendiente"}
    pedidos.append(pedido)
    print("Pedido creado")


# --- NUEVA FUNCIÓN EXTRAÍDA (Refactorización 2) ---
def calcular_totales_pedido(lineas):
    """
    Calcula el desglose económico de un pedido.
    
    Args:
        lineas (list): Lista de diccionarios con los productos, cantidades y precios.
        
    Returns:
        dict: Diccionario que contiene el subtotal, descuento, iva y total calculado.
    """
    suma = 0
    for linea in lineas:
        suma = suma + linea["cantidad"] * linea["precio"]

    descuento = 0
    if suma > UMBRAL_GRANDE:
        descuento = suma * DESCUENTO_GRANDE
    elif suma > UMBRAL_PEQUENO:
        descuento = suma * DESCUENTO_PEQUENO

    iva = (suma - descuento) * IVA
    total = suma - descuento + iva

    return {
        "subtotal": suma,
        "descuento": descuento,
        "iva": iva,
        "total": total
    }
# --------------------------------------------------


def ver_pedidos():
    """
    Imprime por consola un listado de todos los pedidos registrados.
    Muestra el nombre del cliente, el estado del pedido y el total a pagar.
    """
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        pos = 0
        for p in pedidos:
            # Usamos la función extraída
            totales = calcular_totales_pedido(p["lineas"])
            
            print(str(pos + 1) + ". Cliente: " + p["cliente"]["nombre"] + " | Estado: " + p["estado"] + " | Total: " + str(round(totales["total"], 2)) + " €")
            pos = pos + 1


def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    
    # Usamos la función extraída
    totales = calcular_totales_pedido(p["lineas"])

    print("Subtotal: " + str(round(totales["subtotal"], 2)))
    print("Descuento: " + str(round(totales["descuento"], 2)))
    print("IVA: " + str(round(totales["iva"], 2)))
    print("TOTAL: " + str(round(totales["total"], 2)))


def cambiar_estado_pedido():
    # Función sin usar, pensada para detectar código muerto o incompleto
    x = input("Nuevo estado: ")
    return x


# --- CLASES PARA DOCUMENTACIÓN (Ejercicio 8) ---
class ClienteApp:
    """
    Representa a un cliente dentro de la aplicación.
    Almacena datos básicos como el nombre, teléfono y correo electrónico.
    """
    pass

class PedidoApp:
    """
    Define la estructura de un pedido en el sistema.
    Agrupa al cliente asociado, las líneas de compra y el estado actual (pendiente, completado).
    """
    pass
# -----------------------------------------------