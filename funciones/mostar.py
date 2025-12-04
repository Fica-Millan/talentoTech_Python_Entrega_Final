#funciones/mostar.py

"""
Módulo para mostrar productos del inventario.
"""

import sqlite3
from colorama import Fore, Back
import sys
import os

# Agregar el directorio raíz al PATH para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import conectar_bd
from utils.formatear_precio import formatear_precio



def mostrar_productos():
    """
    Muestra todos los productos registrados en el inventario.
    
    Para cada producto muestra:
        - ID
        - Nombre
        - Descripción
        - Cantidad disponible
        - Precio (formateado con separadores de miles y dos decimales)
        - Categoría
    
    Si no hay productos, muestra un mensaje informativo.
    """
    
    # Encabezado visual
    print(f"{Fore.BLUE}\n🔵 LISTA DE PRODUCTOS")
    print(f"{Fore.BLUE}{'━'*89}")
    
    # -----------------------------
    # Conexión a la base de datos
    # -----------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Obtener todos los productos ordenados por ID ascendente
            cursor.execute('SELECT * FROM productos ORDER BY id ASC')
            productos = cursor.fetchall()
            
            # Si no hay registros, avisar al usuario
            if not productos:
                print(f"{Fore.YELLOW}⚠️  No hay productos registrados.")
            else:
                # Recorrer cada fila (producto) y mostrar sus datos formateados
                for producto in productos:
                    id_prod, nombre, descripcion, cantidad, precio, categoria = producto
                    
                    # Convertir precio numérico en una cadena amigable (ej: $ 12.500,00)
                    precio_formateado = formatear_precio(precio)

                    # Mostrar la información del producto
                    print(f"{Fore.BLUE}ID: {Fore.YELLOW}{id_prod}")
                    print(f"{Fore.BLUE}Nombre: {Fore.GREEN}{nombre}")
                    print(f"{Fore.BLUE}Descripción: {descripcion}")
                    print(f"{Fore.BLUE}Cantidad: {cantidad}")
                    print(f"{Fore.BLUE}Precio: {precio_formateado}")
                    print(f"{Fore.BLUE}Categoría: {categoria}")
                    print(f"{Fore.BLUE}{'─'*89}")
                
        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al mostrar productos: {e}")
        
        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()