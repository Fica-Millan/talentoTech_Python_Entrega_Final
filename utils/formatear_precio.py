#  utils/formatear_precio.py

"""
Utilidades para formatear precios
"""

def formatear_precio(precio):
    """
    Formatea un precio con separador de miles (punto) y dos decimales.
    
    Parámetros:
        precio (float): El precio a formatear
        
    Retorna:
        str: Precio formateado como "$ 1.234,56"
    """
    precio_formateado = f"{precio:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"$ {precio_formateado}"