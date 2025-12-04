# funciones/registrar.py

"""
Módulo para agregar productos al inventario.
Incluye funciones para solicitar datos al usuario con validación y registrar
nuevos productos en la base de datos.
"""

import sqlite3
from colorama import Fore, Back
import sys
import os

# Agregar el directorio raíz al PATH para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.db import conectar_bd


# -------------------------------------------------------------------------
# Función genérica para pedir datos
# -------------------------------------------------------------------------
def pedir_dato(mensaje, validar=None, transformar=None):
    """  
    Solicita un dato al usuario, valida el valor ingresado y opcionalmente
    lo transforma antes de retornarlo.

    Parámetros:
        - mensaje: texto que se muestra al pedir input
        - validar: función que recibe el texto ingresado y devuelve True/False
        - transformar: función que transforma el valor final antes de retornarlo

    Retorna:
        El valor ingresado (posiblemente transformado).
    """
    
    while True:
        valor = input(mensaje).strip()

        # Si no hay función de validación, o si el valor es válido
        if validar is None or validar(valor):
            return transformar(valor) if transformar else valor

        # Mensaje estándar de error
        print(f"{Fore.YELLOW}⚠️  Valor inválido, intente nuevamente.")

# -----------------------------------------------
# Función principal: Registrar un producto nuevo
# -----------------------------------------------
def registrar_producto():
    """Solicita los datos de un nuevo producto y lo guarda en la base de datos."""
    
    # Encabezado visual
    print(f"{Fore.GREEN}\n🟢 AGREGAR NUEVO PRODUCTO")
    print(f"{Fore.GREEN}{'━'*89}")
    
    # -----------------------------
    # Solicitar datos al usuario
    # -----------------------------

    # Nombre (no vacío)
    nombre = pedir_dato(
        f"{Fore.GREEN}Nombre del producto: ",
        validar=lambda x: len(x) > 0,
        transformar=lambda x: x.title()
    )

    # Descripción (máx 100 caracteres)
    descripcion = pedir_dato(
        f"{Fore.GREEN}Descripción (máx 100 caracteres): ",
        validar=lambda x: len(x) > 0 and len(x) <= 100,
        transformar=lambda x: x.capitalize(),
    )

    # Cantidad (entero >= 0)
    cantidad = pedir_dato(
        f"{Fore.GREEN}Cantidad: ",
        validar=lambda x: x.isdigit() and int(x) >= 0,
        transformar=lambda x: int(x)
    )

    # Precio (float > 0)
    def validar_precio(x):
        """Valida que el precio sea un número flotante mayor a cero."""
        try:
            return float(x) > 0
        except ValueError:
            return False

    precio = pedir_dato(
        f"{Fore.GREEN}Precio: $ ",
        validar=validar_precio,
        transformar=lambda x: float(x)
    )

    # Categoría (no vacía)
    categoria = pedir_dato(
        f"{Fore.GREEN}Categoría: ",
        validar=lambda x: len(x) > 0,
        transformar=lambda x: x.title()
    )

    # -----------------------------
    # Guardar en la base de datos
    # -----------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Inserción en tabla productos
            cursor.execute('''
                INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, cantidad, precio, categoria))

            conexion.commit()            
            print(f"\n{Fore.GREEN}✅ Producto '{nombre}' registrado exitosamente.")
                  
        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al agregar producto: {e}")

        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()
