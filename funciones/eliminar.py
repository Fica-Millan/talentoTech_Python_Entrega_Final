#funciones/eliminar.py

"""
Módulo para eliminar productos del inventario.
"""

import sqlite3
from colorama import Fore, Back
import sys
import os

# Agregar el directorio raíz al PATH para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import conectar_bd



def eliminar_producto():
    """
    Elimina un producto del inventario por su ID.
    
    Proceso:
        1. Muestra lista de productos disponibles
        2. Solicita ID del producto a eliminar con validación
        3. Solicita confirmación al usuario
        4. Elimina el producto si se aprueba la confirmación
    
    Incluye validaciones para evitar errores y eliminaciones accidentales.
    """
    
    # Encabezado visual
    print(f"{Fore.RED}\n🔴 ELIMINAR PRODUCTO")
    print(f"{Fore.RED}{'━'*89}")
    
    # -----------------------------
    # Conexión a la base de datos
    # -----------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Obtener lista de productos (solo ID y nombre para simplificar)
            cursor.execute('SELECT id, nombre FROM productos')
            productos = cursor.fetchall()
            
            # Si no hay productos registrados, no se puede eliminar nada
            if not productos:
                print(f"{Fore.YELLOW}⚠️  No hay productos para eliminar.")
                return
            
            # Mostrar productos disponibles para seleccionar
            print(f"\n{Fore.RED}Productos disponibles:")
            for prod in productos:
                print(f"{Fore.RED}  ID: {prod[0]} - {prod[1]}{Fore.RESET}")
            
            # -----------------------------
            # Solicitar ID y validar entrada
            # -----------------------------
            while True:
                try:
                    id_producto = int(input(f"\n{Fore.RED}ID del producto a eliminar: ").strip())
                    
                    # Verificar si el ID existe realmente
                    cursor.execute('SELECT nombre FROM productos WHERE id = ?', (id_producto,))
                    resultado = cursor.fetchone()
                    
                    if resultado:
                        nombre_producto = resultado[0]
                        break  # ID válido → continuar
                    else:
                        print(f"{Fore.YELLOW}⚠️  No existe un producto con ese ID. Intente nuevamente")
                    
                except ValueError:
                    # Mensaje para cuando el usuario ingresa algo no convertible a entero
                    print(f"{Back.RED}❌ Debe ingresar un número válido.")
            
            # -----------------------------
            # Confirmación del usuario
            # -----------------------------
            confirmacion = input(f"{Fore.YELLOW}\n⚠️  ¿Confirma eliminar '{nombre_producto}'? (s/n): ").strip().lower()
            
            # Si confirma → eliminar producto
            if confirmacion in ("s", "si", "sí"):
                cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
                conexion.commit()
                print(f"\n{Fore.GREEN}✅ Producto '{nombre_producto}' eliminado correctamente.")
            
            # Si no confirma → cancelar operación
            else:
                print(f"\n{Fore.CYAN}ℹ️  Operación cancelada.")
            
        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al eliminar producto: {e}")
        
        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()