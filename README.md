<p align="center">
  <img src="assets/banner_sistema_inventario.png" width="100%" />
</p>

<div align="center">

   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
   ![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite&logoColor=white)
   ![Colorama](https://img.shields.io/badge/Colorama-Enabled-yellow)
   ![Status](https://img.shields.io/badge/Status-Terminado-green)
   ![Author](https://img.shields.io/badge/Autor-Yesica%20Fica%20Mill%C3%A1n-purple)

</div>

<h1>Sistema de Gestión de Inventario en Python</h1>

Proyecto desarrollado como **Trabajo Final Integrador** del curso
**Iniciación a la Programación en Python — Talento Tech**.


<h3>📚 Índice<h3>

- [Descripción General](#descripción-general)
- [Requisitos](#requisitos)
  - [Software necesario](#software-necesario)
  - [Librerías necesarias](#librerías-necesarias)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
  - [En Windows:](#en-windows)
  - [En Linux/Mac:](#en-linuxmac)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
  - [1. ✅ Registro de Productos](#1--registro-de-productos)
  - [2. ✅ Mostrar Productos](#2--mostrar-productos)
  - [3. ✅ Actualización de Productos](#3--actualización-de-productos)
  - [4. ✅ Eliminación de Productos](#4--eliminación-de-productos)
  - [5. ✅ Búsqueda de Productos](#5--búsqueda-de-productos)
  - [6. ✅ Reporte de Bajo Stock](#6--reporte-de-bajo-stock)
- [Base de Datos](#base-de-datos)
  - [Estructura de la tabla `productos`](#estructura-de-la-tabla-productos)
- [Interfaz de Usuario](#interfaz-de-usuario)
- [Características Técnicas](#características-técnicas)
- [Ejemplos de Uso](#ejemplos-de-uso)
  - [Agregar un Producto](#agregar-un-producto)
  - [Buscar un Producto](#buscar-un-producto)
  - [Generar Reporte de Bajo Stock](#generar-reporte-de-bajo-stock)
- [Mejoras Futuras](#mejoras-futuras)
- [Notas Importantes](#notas-importantes)
- [Autor](#autor)

## Descripción General

<hr style="border: 1px solid #34C759;">

Sistema completo de gestión de inventario desarrollado en Python que permite:
- Registrar productos
- Mostrar productos
- Buscar por ID
- Actualizar cantidad
- Eliminar registros
- Generar reporte de bajo stock

El sistema utiliza **SQLite** como base de datos local, **colorama** para mejorar la interfaz por consola y una **arquitectura modular** basada en funciones organizadas por carpetas.

## Requisitos

<hr style="border: 1px solid #34C759;">

### Software necesario
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Librerías necesarias
```bash
pip install colorama
```

> La librería `sqlite3` viene incluida con Python, no requiere instalación adicional.

## Estructura del Proyecto

<hr style="border: 1px solid #34C759;">


```
proyecto_inventario/
│
├── main.py                         # Programa principal con el menú
│
├── funciones/
│   ├── mostrar.py                  # Muestra todos los productos
│   ├── registrar.py                # Registra nuevos productos
│   ├── actualizar.py               # Actualiza cantidades
│   ├── eliminar.py                 # Elimina productos por ID
│   ├── buscar.py                   # Búsqueda por ID
│   └── reporte.py                  # Reporte de bajo stock
│
├── utils/
│   ├── colores.py                  # Almacena colores adicionales
│   ├── db.py                       # Conexión y creación de la base
│   ├── formatear_precio.py         # Formateo de precios
│   └── mostrar_menu.py             # Muestra el menú principal
│
├── inventario.db                   # Base SQLite (se genera automáticamente)
└── README.md                       # Documentación del proyecto
```

## Instalación

<hr style="border: 1px solid #34C759;">

1. **Descargar el proyecto**
   - Descomprime el archivo .zip en la carpeta de tu elección

2. **Instalar dependencias**
   ```bash
   pip install colorama
   ```

3. **Verificar Python**
   ```bash
   python --version
   ```

## Ejecución

<hr style="border: 1px solid #34C759;">

### En Windows:
```bash
python main.py
```

### En Linux/Mac:
```bash
python3 main.py
```

## Funcionalidades Implementadas

<hr style="border: 1px solid #34C759;">

### 1. ✅ Registro de Productos
- Solicita: nombre, descripción, cantidad, precio y categoría
- Validaciones:
  - Nombre no puede estar vacío
  - Cantidad debe ser un número entero positivo o cero
  - Precio debe ser un número positivo mayor a cero
  - Categoría no puede estar vacía

### 2. ✅ Mostrar Productos
- Muestra todos los productos registrados
- Incluye: ID, nombre, descripción, cantidad, precio y categoría
- Formato de precio con separador de miles

### 3. ✅ Actualización de Productos
- Permite actualizar la cantidad disponible
- Busca por ID del producto
- Muestra lista de productos disponibles
- Valida que el ID exista

### 4. ✅ Eliminación de Productos
- Elimina productos por ID
- Solicita confirmación antes de eliminar
- Muestra lista de productos disponibles
- Previene eliminaciones accidentales

### 5. ✅ Búsqueda de Productos
- Métodos de búsqueda disponibles:
        1. Por ID (coincidencia exacta)
        2. Por Nombre (coincidencia parcial)
        3. Por Categoría (coincidencia parcial)
- Muestra información completa del producto encontrado
- Mensaje claro si no se encuentra el producto

### 6. ✅ Reporte de Bajo Stock
- Genera reporte de productos con cantidad igual o inferior al límite especificado
- El usuario define el límite de stock
- Destaca productos críticos 

## Base de Datos

<hr style="border: 1px solid #34C759;">

### Estructura de la tabla `productos`

| Campo       | Tipo    | Descripción                           |
|-------------|---------|---------------------------------------|
| id          | INTEGER | Clave primaria, autoincremental       |
| nombre      | TEXT    | Nombre del producto (no nulo)         |
| descripcion | TEXT    | Descripción del producto              |
| cantidad    | INTEGER | Cantidad disponible (no nulo)         |
| precio      | REAL    | Precio del producto (no nulo)         |
| categoria   | TEXT    | Categoría del producto                |

La base **se crea automáticamente** en la primera ejecución del programa.

## Interfaz de Usuario

<hr style="border: 1px solid #34C759;">

El sistema utiliza:
- **Menú interactivo** en línea de comandos:
   - 🟢 Registrar producto: registrar un nuevo producto en la base de datos.
   - 🔵 Mostrar productos: mostrar todos los productos cargados.
   - 🟠 Actualizar cantidad: actualizar la cantidad en stock de un producto existente.
   - 🔴 Eliminar producto: eliminar un producto por ID.
   - 🟡 Buscar producto: buscar productos por ID, nombre o categoría.
   - 🟣 Reporte productos con bajo stock: generar un reporte de productos con stock por debajo de un límite elegido.
   - ⚫ Salir: salir de la aplicación.
- **Colorama** para mejorar la experiencia visual:
   - CYAN → Visualización general
   - YELLOW → Advertencias
   - GREEN → Confirmaciones
   - RED → Errores y eliminaciones

## Características Técnicas

<hr style="border: 1px solid #34C759;">

🟢 Código Modular
- Cada acción está separada en un archivo dentro de funciones/.
- utils/ contiene funciones de apoyo (conexión a DB y formateo).

🟢 Manejo de Errores
- Validación de inputs
- Manejo de excepciones de SQLite
- Mensajes claros y amigables

🟢 Seguridad
- Consultas SQL parametrizadas
- Confirmación en operaciones críticas

🟢  Persistencia
- SQLite garantiza la permanencia de los datos entre ejecuciones.

## Ejemplos de Uso

<hr style="border: 1px solid #34C759;">

### Agregar un Producto
```
Opción: 1
Nombre del producto: Fideos
Descripción: Tirabuzon 500gr marca Matarazzo 
Cantidad: 10
Precio: $ 1678.50
Categoría: Almacen
```

### Buscar un Producto
```
Opción: 5
ID del producto a buscar: 1
```

### Generar Reporte de Bajo Stock
```
Opción: 6
Ingrese el límite de stock: 15
```

## Mejoras Futuras

<hr style="border: 1px solid #34C759;">

- [ ] Exportar reportes a CSV
- [ ] Interfaz gráfica (GUI)
- [ ] Sistema de usuarios y permisos
- [ ] Historial de movimientos
- [ ] Código de barras

## Notas Importantes

<hr style="border: 1px solid #34C759;">

1. La base de datos `inventario.db` se crea automáticamente en la primera ejecución
2. No elimines el archivo `inventario.db` si quieres conservar los datos
3. Para reiniciar con base limpia, elimina `inventario.db`
4. Los precios se formatean automáticamente con separador de miles

## Autor

<hr style="border: 1px solid #34C759;">

Este proyecto fue creado por [Fica](https://github.com/Fica-Millan).

¡Siéntete libre de contactarme si tienes alguna pregunta o sugerencia!

[LinkedIn](https://www.linkedin.com/in/yesica-fica-millan/)
