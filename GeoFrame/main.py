# ----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" App: Optimización y Cálculo de Medidas para Ventana Normanda """

# NOTE: Ultima Modificación: 11/12/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Materia: Matemáticas III
# NOTE: Grupo: 3° "J"
# NOTE: Correo (Soporte/Comentarios): cgmagallanes23@gmail.com

# ----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
from app.geoframe import GeoFrame                                             # Importamos la Clase de la App
import matplotlib.pyplot as graphics                                          # Librería Principal para Gráficos y Visualizaciones

# ----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Función Principal ============================================================= """

# Función: Punto de Entrada
def main() -> None:
    
    """
        - Método: Punto de Entrada
        - Argumentos: Ninguno
        - Retorno: Ninguno
        - Objetivo Principal: Punto de Entrada de Ejecución de la App
    """
    
    # App de Optimización de Ventana Normanada 
    GeoFrame()
    
    # Mostrar Gráficas de Matplotlib
    graphics.show()


# ----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Ejecución de App ============================================================= """

# Ejecutar la Aplicación
if __name__ == "__main__": main()

# ----------------------------------------------------------------------------------------------------------------------------------------