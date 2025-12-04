# utils/db.py

"""
Utilidades para gestión de base de datos
"""

import sqlite3
from colorama import Back

def conectar_bd():
    """
    Establece conexión con la base de datos inventario.db
    
    Retorna:
        sqlite3.Connection: Objeto de conexión o None si hay error
    """
    try:
        # Intentar conectar a la base de datos local
        conexion = sqlite3.connect('inventario.db')
        return conexion
    except sqlite3.Error as e:
        # Mensaje visual en caso de error de conexión
        print(f"{Back.RED}❌ Error al conectar con la base de datos: {e}")
        return None

def crear_tabla():
    """
    Crea la tabla productos si no existe en la base de datos.
    
    Estructura:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        - descripcion: TEXT (máx 100 caracteres)
        - cantidad: INTEGER NOT NULL
        - precio: REAL NOT NULL
        - categoria: TEXT
    """
    
    # Se obtiene la conexión usando la función reutilizable
    conexion = conectar_bd()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Comando SQL para crear la tabla solo si no existe
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT CHECK (LENGTH(descripcion) <= 100),
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                )
            ''')
            
            # Guardar cambios en la base de datos
            conexion.commit()
            
        except sqlite3.Error as e:
            # Error general al intentar crear la tabla
            print(f"{Back.RED}❌ Error al crear tabla: {e}")
            
        finally:
            # Cerrar conexión para evitar bloqueos de la base de datos
            conexion.close()
            