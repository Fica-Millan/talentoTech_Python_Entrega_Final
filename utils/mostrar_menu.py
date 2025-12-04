# utils/mostrar_menu.py

from colorama import init, Fore
from utils.colores import ColoresExtra

def mostrar_menu():
    """Muestra el menú principal"""
    
    # Encabezado del menú
    print(f"{Fore.CYAN}\nMENÚ PRINCIPAL")
    print(f"{Fore.CYAN}{'━'*89}")

    # Opción para registrar un nuevo producto en la base de datos
    print(f"{Fore.CYAN}1. 🟢 Registrar producto")

    # Opción para mostrar todos los productos cargados
    print(f"{Fore.CYAN}2. 🔵 Mostrar productos")

    # Opción para actualizar la cantidad en stock de un producto existente
    print(f"{Fore.CYAN}3. 🟠 Actualizar cantidad{Fore.RESET}")

    # Opción para eliminar un producto por ID
    print(f"{Fore.CYAN}4. 🔴 Eliminar producto")

    # Opción para buscar productos por ID, nombre o categoría
    print(f"{Fore.CYAN}5. 🟡 Buscar producto")

    # Opción para generar un reporte de productos con stock por debajo de un límite elegido
    print(f"{Fore.CYAN}6. 🟣 Reporte productos con bajo stock")

    # Opción para salir de la aplicación
    print(f"{Fore.CYAN}7. ⚫ Salir")

    # Línea de cierre del menú
    print(f"{Fore.CYAN}{'━'*89}")