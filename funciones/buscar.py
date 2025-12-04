#funciones/buscar.py

"""
Módulo para buscar productos en el inventario
"""

import sqlite3
from colorama import Fore, Back
import sys
import os

# Agregar el directorio raíz al PATH para permitir importar módulos desde utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import conectar_bd
from utils.formatear_precio import formatear_precio



def buscar_producto():
    """      
    Permite buscar productos mediante diferentes criterios.
    
    Métodos de búsqueda disponibles:
        1. Por ID (coincidencia exacta)
        2. Por Nombre (coincidencia parcial)
        3. Por Categoría (coincidencia parcial)
    
    Muestra:
        - Lista de productos que coinciden con el criterio elegido
        - Un mensaje si no se encuentran coincidencias
    """
    
    # Encabezado visual
    print(f"{Fore.YELLOW}\n🟡 BUSCAR PRODUCTO")
    print(f"{Fore.YELLOW}{'━'*89}")
      
    # ------------------------------------------------------  
    # Seleccionar método de búsqueda (ID, nombre, categoría)
    # ------------------------------------------------------
    while True:
        print(f"""
        {Fore.YELLOW}Seleccione el tipo de búsqueda:

        1. Buscar por ID
        2. Buscar por Nombre
        3. Buscar por Categoría
        """)

        opcion = input(f"{Fore.YELLOW}Ingrese opción (1-3): ").strip()

         # Validar opción ingresada
        if opcion in ("1", "2", "3"):
            break  # Opción válida, salimos del bucle
        else:
            print(f"{Fore.YELLOW}⚠️  Opción inválida. Intente nuevamente.\n")
        

    # ------------------------------------------------------------------
    # Solicitar el dato según el tipo de búsqueda seleccionado
    # ------------------------------------------------------------------
    if opcion == "1":
        # -----------------------
        # Búsqueda por ID (entero)
        # -----------------------
        while True:
            try:
                valor = int(input(f"{Fore.YELLOW}Ingrese ID: ").strip())
                campo = "id"
                valor_bd = valor
                break
            except ValueError:
                print(f"{Back.RED}❌ Debe ingresar un número válido.")

    elif opcion == "2":
        # --------------------------------------
        # Búsqueda por nombre (coincidencia parcial)
        # --------------------------------------
        valor = input(f"{Fore.YELLOW}Ingrese nombre o parte del nombre: ").strip()
        campo = "nombre"
        valor_bd = f"%{valor}%"   # Busca coincidencias parciales

    elif opcion == "3":
        # --------------------------------------
        # Búsqueda por categoría (parcial)
        # --------------------------------------
        valor = input(f"{Fore.YELLOW}Ingrese categoría: ").strip()
        campo = "categoria"
        valor_bd = f"%{valor}%"

    # --------------------------------------
    # Ejecutar búsqueda en la base de datos
    # --------------------------------------
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Generar consulta dinámica según el campo elegido
            query = f"SELECT * FROM productos WHERE {campo} LIKE ?" if campo != "id" else \
                    "SELECT * FROM productos WHERE id = ?"

            cursor.execute(query, (valor_bd,))
            resultados = cursor.fetchall()

            # ----------------------------------
            # Mostrar resultados de la búsqueda
            # ----------------------------------
            if resultados:
                print(f"\n{Fore.YELLOW}Resultados encontrados:")
                print(f"{Fore.YELLOW}{'━'*89}")

                for producto in resultados:
                    id_prod, nombre, descripcion, cantidad, precio, categoria = producto
                    precio_formateado = formatear_precio(precio)

                    print(f"""
                    {Fore.YELLOW}ID: {id_prod}
                    Nombre: {nombre}
                    Descripción: {descripcion}
                    Cantidad: {cantidad}
                    Precio: {precio_formateado}
                    Categoría: {categoria}
                    """)
            else:
                # No se encontraron coincidencias
                print(f"{Fore.WHITE}\n⚠️  No se encontraron productos que coincidan con su búsqueda.")

        except sqlite3.Error as e:
            # Error al ejecutar la consulta o acceder a la base de datos
            print(f"{Back.RED}❌ Error al buscar producto: {e}")

        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()
