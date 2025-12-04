"""
Trabajo Final Integrador - Sistema de Gestión de Inventario
Autor: Yesica Fica Millán
Curso: Iniciación a la programación en Python | Talento Tech
Descripción: Sistema completo de gestión de inventario con base de datos SQLite
"""

import sqlite3
from colorama import init, Fore, Back, Style
from funciones.registrar import registrar_producto
from funciones.mostar import mostrar_productos     
from funciones.actualizar import actualizar_producto
from funciones.eliminar import eliminar_producto
from funciones.buscar import buscar_producto
from funciones.reporte import reporte_bajo_stock
from utils.mostrar_menu import mostrar_menu
from utils.db import crear_tabla

# Inicializar colorama
init(autoreset=True)

# Programa principal
if __name__ == "__main__":
    # Crear tabla si no existe
    crear_tabla()
    
    # Mensaje de bienvenida
    print(f"{Fore.CYAN}\n\nB I E N V E N I D O   A L   S I S T E M A   D E   G E S T I Ó N   D E   P R O D U C T O S")
    print(f"{Fore.CYAN}{'*'*89}")
    
    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input(f"\n{Fore.CYAN}Seleccione una opción: ").strip()
        
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print(f"\n{Fore.CYAN}{'━'*89}")
            print(f"{Fore.CYAN}🛑 Cerrando el sistema...")
            print(f"{Fore.CYAN}✅ Operación finalizada con éxito.\n\n")
            break
        else:
            print(f"\n{Back.RED}❌ Opción inválida. Debe elegir entre 1 y 7.")