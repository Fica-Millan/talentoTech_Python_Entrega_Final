# funciones/reporte.py

"""
Módulo para generar reportes del inventario.
Incluye funciones para consultar productos con bajo stock.
"""

import sqlite3
from colorama import Fore, Back
import sys
import os

# Agregar el directorio raíz al path para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import conectar_bd
from utils.formatear_precio import formatear_precio



def reporte_bajo_stock():
    """     
    Genera un reporte de productos cuyo stock es menor o igual a un límite definido por el usuario.

    Flujo:
        1. Solicita al usuario un valor numérico (límite de stock).
        2. Consulta en la base de datos los productos con cantidad <= límite.
        3. Muestra los resultados formateados.
        4. Si no hay productos bajo el límite, informa al usuario.

    Manejo de errores:
        - Valida que el límite sea un número entero válido.
        - Controla errores al acceder a la base de datos.
    """
    
    # Encabezado visual
    print(f"{Fore.MAGENTA}\n🟣 REPORTE PRODUCTOS CON BAJO STOCK")
    print(f"{Fore.MAGENTA}{'━'*89}")
    
    # -----------------------------
    # Solicitar y validar el límite
    # -----------------------------
    while True:
        try:
            limite = int(input(f"\n{Fore.MAGENTA}¿Mostrar productos con menos de cuántas unidades?: ").strip())

            if limite >= 0:
                break
            print(f"{Fore.YELLOW}⚠️  El límite debe ser un número positivo o cero.")
        except ValueError:
            print(f"{Fore.YELLOW}⚠️  Debe ingresar un número válido.")
    
    
    # -----------------------------
    # Conexión a la base de datos
    # -----------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Obtener productos con cantidad <= límite
            cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (limite,))
            productos = cursor.fetchall()
            
            # -----------------------------
            # Mostrar resultados
            # -----------------------------
            if not productos:
                print(f"\n{Fore.MAGENTA}✅ No hay productos con stock igual o menor a {limite}.")
            else:
                print(f"\n{Fore.YELLOW}⚠️  Productos con bajo stock: \n")
                for producto in productos:
                    id_prod, nombre, descripcion, cantidad, precio, categoria = producto
                    precio_formateado = formatear_precio(precio)
                    
                    print(f"{Fore.MAGENTA}ID: {Fore.MAGENTA}{id_prod}")
                    print(f"{Fore.MAGENTA}Nombre: {Fore.MAGENTA}{nombre}")
                    print(f"{Fore.MAGENTA}Cantidad: {Fore.MAGENTA}{cantidad}")
                    print(f"{Fore.MAGENTA}Precio: {precio_formateado}")
                    print(f"{Fore.MAGENTA}Categoría: {categoria}")
                    print(f"\n{Fore.MAGENTA}{'━'*89}")
                    
        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al generar reporte: {e}")
            
        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()