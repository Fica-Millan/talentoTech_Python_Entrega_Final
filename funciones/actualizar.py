#funciones/actualizar.py

"""
Módulo para actualizar productos del inventario.
"""

import sqlite3
from colorama import Fore, Back
import sys
import os
from utils.colores import ColoresExtra

# Agregar el directorio raíz al PATH para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import conectar_bd



def actualizar_producto():
    """
    Actualiza la cantidad disponible de un producto existente.
    
     Proceso:
        1. Muestra todos los productos junto con su stock actual
        2. Solicita al usuario el ID del producto que desea modificar
        3. Solicita la nueva cantidad a asignar
        4. Actualiza la base de datos con la nueva cantidad

    Validaciones:
        - El ID ingresado debe existir en la tabla productos
        - La cantidad debe ser un número entero mayor o igual a 0
    """
    
    # Encabezado visual
    print(f"{ColoresExtra.ORANGE}\n🟠 ACTUALIZAR CANTIDAD DE PRODUCTO{Fore.RESET}")
    print(f"{ColoresExtra.ORANGE}{'━'*89}{Fore.RESET}")
    
    # -----------------------------
    # Conexión a la base de datos
    # -----------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Obtener listado de productos para mostrar al usuario
            cursor.execute('SELECT id, nombre, cantidad FROM productos')
            productos = cursor.fetchall()
            
            # Verificar si la tabla está vacía
            if not productos:
                print(f"{Fore.YELLOW}⚠️  No hay productos para actualizar.")
                return
            
            # Mostrar productos disponibles con su stock actual
            print(f"\n{ColoresExtra.ORANGE}Productos disponibles:{Fore.RESET}")
            for prod in productos:
                print(f"{ColoresExtra.ORANGE}  ID: {prod[0]} - {prod[1]} (Stock actual: {prod[2]}){Fore.RESET}")
            
            # -------------------------------------------------------------------------
            # Solicitar ID del producto a actualizar (debe existir en la base de datos)
            # -------------------------------------------------------------------------
            while True:
                try:
                    id_producto = int(
                        input(f"\n{ColoresExtra.ORANGE}ID del producto a actualizar: {Fore.RESET}")
                        .strip())
                    
                    # Comprobar si el ID existe en la base
                    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
                    if cursor.fetchone():
                        break # ID válido, continuar
                    
                    print(f"{Fore.YELLOW}⚠️  No existe un producto con ese ID. Intente nuevamente")
                
                except ValueError:
                    print(f"{Back.RED}❌ Debe ingresar un número válido.")
            
            # -------------------------------------------------------------
            # Solicitar nueva cantidad (entero >= 0)
            # -------------------------------------------------------------
            while True:
                try:
                    nueva_cantidad = int(input(f"{ColoresExtra.ORANGE}Nueva cantidad: {Fore.RESET}").strip())
                    if nueva_cantidad >= 0:
                        break # Cantidad válida, continuar
                    
                    print(f"{Fore.YELLOW}⚠️  La cantidad debe ser un número positivo o cero.")
                
                except ValueError:
                    print(f"{Back.RED}❌ Debe ingresar un número entero válido.")
            
            # -------------------------------------------------------------
            # Actualizar registro en la base de datos
            # -------------------------------------------------------------
            cursor.execute(
                'UPDATE productos SET cantidad = ? WHERE id = ?', 
                (nueva_cantidad, id_producto))
            conexion.commit()
            
            print(f"\n{Fore.GREEN}✅ Cantidad actualizada correctamente.")
            
        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al actualizar producto: {e}")
            
        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()