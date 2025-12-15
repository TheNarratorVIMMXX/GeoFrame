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
from pathlib import Path                                             # Manejo de Rutas y Archivos
from typing import *                                                 # Tipos de Datos 
from matplotlib.collections import PatchCollection                   # Colección de Parches para Gráficos de Matplotlib
from matplotlib.patches import Rectangle, Wedge                      # Herramientas para Dibujar Formas Geométricas de Matplotlib
from matplotlib.widgets import Slider, Button, RadioButtons          # Controles Interactivos de Matplotlib
from scipy.optimize import minimize_scalar                           # Función de Optimización Avanzada de Scipy
from PyQt5.QtGui import QIcon                                        # Iconos para la Ventana de la App de PyQt5
import matplotlib.patheffects as fig_effects                         # Efectos Visuales para Texto y Gráficos de Matplotlib
import matplotlib.pyplot as graphics                                 # Librería Principal para Gráficos y Visualizaciones de Matplotlib
import numpy                                                         # Librería para Cálculos Numéricos Avanzados
import seaborn as app_style                                          # Estilos Profesionales para Gráficos de Seaborn

# ----------------------------------------------------------------------------------------------------------------------------------------
""" ================================================== Configuraciones Adicionales ======================================================= """
                  
# Configuración Global de Fuente para Gráficas
graphics.rcParams['font.family'] = 'serif'                           # Fuente Serif para Gráficas
graphics.rcParams['font.serif'] = 'Times New Roman'                  # Fuente Times New Roman para Gráficas

# ----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Clase: GeoFrame (Optimizador de Ventana Normanda)
class GeoFrame:
    
    """
        - Clase: GeoFrame (App de Optimización de Ventana Normanda)
        - Atributos:
            - window (matplotlib.pyplot.Figure): Ventana Principal de la App GeoFrame
            - controls_panel (matplotlib.pyplot.Axes): Panel de Controles de la App GeoFrame
            - normand_window_panel (matplotlib.pyplot.Axes): Panel de Visualización de la Ventana Normanda
            - area_graphic_panel (matplotlib.pyplot.Axes): Panel de Gráfica de Área vs X
            - results_panel (matplotlib.pyplot.Axes): Panel de Resultados Numéricos Detallados
            - sensibility_panel (matplotlib.pyplot.Axes): Panel de Análisis de Sensibilidad
            - slider_panel (matplotlib.pyplot.Axes): Panel para el Slider Interactivo
            - slider (matplotlib.widgets.Slider): Slider Interactivo para el Perímetro
            - radio_panel (matplotlib.pyplot.Axes): Panel para los Botones de Radio
            - radio (matplotlib.widgets.RadioButtons): Botones de Radio para Modo de Visualización
            - perimeter (float): Perímetro de la Ventana Normanda (Metros)
            - norman_window_x (float | None): Dimensión Óptima X (Ancho) de la Ventana Normanda (Metros)
            - norman_window_y (float | None): Dimensión Óptima Y (Altura) de la Ventana Normanda (Metros)
            - max_area (float | None): Área Máxima Calculada de la Ventana Normanda (Metros Cuadrados)
            - perimeters_record (list[float]): Historial de Perímetros Calculados
            - areas_record (list[float]): Historial de Áreas Calculadas
            - visualization_mode (Literal["Normal", "Detallado", "Técnico"]): Modo de Visualización
            - buttons (list[matplotlib.pyplot.Button]): Lista de Botones de la Ventana
            - text_stats (list[matplotlib.pyplot.Text]): Estadísticas en Texto
            - _last_perimeter (float | None): Último Perímetro Calculado
            - _cached_dimensions (tuple[float, float, float] | None): Cache de Dimensiones Óptimas
            - _sensibility_cache_perimeters (numpy.ndarray | None): Caché de Perímetros Precalculados
            - _sensibility_cache_areas (numpy.ndarray | None): Caché de Áreas Precalculadas
        - Métodos:
            - __init__(self) -> None: Inicializador de la App
            - _configure_window_elements(self) -> None: Configurador de Elementos de la Ventana
            - _configure_controls(self) -> None: Configurar Controles
            - _optmize_dimensions(self, perimeter: float | int) -> float | int: Optimizar Dimensiones
            - _draw_normand_window(self) -> None: Dibujar Ventana Normanda
            - _graph_area_vs_widht(self) -> None: Gráfica de Área vs Ancho
            - _see_results(self) -> None: Mostrar Resultados Numéricos
            - _graph_sensibility(self) -> None: Gráfica de Análisis de Sensibilidad
            - _change_visualization_mode(self, mode: str) -> None: Cambiar Modo de Visualización
            - _update_all(self, event) -> None: Actualizar Todo
            - _on_slider_release(self, event) -> None: Evento al Soltar el Slider
            - _initialize_sensibility_cache(self) -> None: Inicializar Caché de Sensibilidad
        - Objetivo: Hallar las Dimesniones Óptimas de una Ventana Normanda para Maximizar su Área con una Restricción de Perímetro dada.
    """
    

    # Atributos de la Clase
    __slots__ = (

        # Paneles y Figuras de la Ventana 
        'window',                                        # Ventana Principal de la App (graphics.Figure)
        '_DISTRIBUTION_GRID',                            # Cuadrícula de Distribución Avanzada (graphics.GridSpec)
        'controls_panel',                                # Panel de Controles (graphics.Axes)
        'normand_window_panel',                          # Panel de Visualización (graphics.Axes)
        'area_graphic_panel',                            # Panel de Gráfica de Área vs X (graphics.Axes)
        'results_panel',                                 # Panel de Resultados Numéricos (graphics.Axes)
        'sensibility_panel',                             # Panel de Análisis de Sensibilidad (graphics.Axes)
        'slider_panel',                                  # Panel para el Slider Interactivo (graphics.Axes)
        'radio_panel',                                   # Panel para los Botones de Radio (graphics.Axes)
        
        # Controles Interactivos 
        'slider',                                        # Slider Interactivo para el Perímetro (Slider)
        'radio',                                         # Botones de Radio para Modo de Visualización (RadioButtons)
        'buttons',                                       # Lista de Botones de la Ventana (list[Button])
        
        # Datos y Estado de la Optimización 
        'perimeter',                                     # Perímetro de la Ventana Normanda (float)
        'norman_window_x',                               # Dimensión Óptima X (Ancho) (float | None)
        'norman_window_y',                               # Dimensión Óptima Y (Altura) (float | None)
        'max_area',                                      # Área Máxima Calculada (float | None)
        'perimeters_record',                             # Historial de Perímetros (list[float])
        'areas_record',                                  # Historial de Áreas (list[float])
        'visualization_mode',                            # Modo de Visualización (Literal["Normal", "Detallado", "Técnico"])
        'text_stats',                                    # Estadísticas en Texto (list[Text])
    
        # Caché de Resultados para Optimización
        '_last_perimeter',                               # Último Perímetro Calculado (float | None)
        '_cached_dimensions',                            # Tupla de Dimensiones Óptimas (tuple[float, float, float] | None)
        '_sensibility_cache_perimeters',                 # Perímetros precalculados (numpy.ndarray | None)
        '_sensibility_cache_areas',                      # Áreas precalculadas (numpy.ndarray | None)

    )




    # Método: Inicializador de la App
    def __init__(self) -> None:
        
        """
           - Método: Inicializador de la App GeoFrame
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Inicialización de la App GeoFrame
        """

        # Configuramos Estilo Avanzado para Gráficas
        app_style.set_theme(                                                          # Aplicamos con Seaborn un Tema Profesional
                
            style = 'darkgrid',                                                       # Estilo de Fondo Oscuro con Rejilla
            palette = "colorblind"                                                    # Paleta de Colores 
                
        )
            
        # Atirbutos de la App
        self.window: graphics.Figure = graphics.figure(                                # Figura Principal (Tipo Ventana)
                
            num = 'Optimizador de Ventana Normanda',                                   # Título de la Ventana
            figsize = (19, 10.6),                                                      # Dimensiones de la Ventana (W, H en Pulgadas)

        )                  
        self._DISTRIBUTION_GRID: graphics.GridSpec = self.window.add_gridspec(         # Cuadrícula de Distribución Avanzada
                
            nrows = 4, ncols = 3,                                                      # 4 Filas y 3 Columnas
            hspace = 0.35, wspace = 0.35,                                              # Espaciado Horizontal y Vertical
            left = 0.06, right = 0.97, top = 0.92, bottom = 0.08                       # Márgenes Personalizados

        )
        self.controls_panel: graphics.Axes = self.window.add_subplot(                  # Panel de Controles Principales
                
            self._DISTRIBUTION_GRID[0, 0 : 2]                                          # Ocupa toda la Fila 1 ([0, 0], [0, 1], [0, 2])
                
        )
        self.normand_window_panel: graphics.Axes = self.window.add_subplot(            # Panel de Visualización de Ventana Normanda
                
            self._DISTRIBUTION_GRID[1 : 3, 0]                                          # Ocupa Fila 2 y 3 en Columna ([1,0], [2,0])
                
        )
        self.area_graphic_panel: graphics.Axes = self.window.add_subplot(              # Panel de Gráfica de Área vs Ancho
                
            self._DISTRIBUTION_GRID[1, 1]                                              # Ocupa Fila 2 en Columna 2 ([1,1])
                
        )
        self.results_panel: graphics.Axes = self.window.add_subplot(                   # Panel de Resultados Numéricos Detallados
                
            self._DISTRIBUTION_GRID[0 : 2, 2]                                          # Ocupa Fila 3 en Columna 1([0,2])
                
        )
        self.sensibility_panel: graphics.Axes = self.window.add_subplot(               # Panel de Análisis de Sensibilidad
                
            self._DISTRIBUTION_GRID[2, 2]                                              # Ocupa Fila 3 en Columna 3 ([2,2])
                
        )
        self.slider_panel: graphics.Axes = graphics.axes(                              # Panel para el Slider Interactivo
                
            arg = [0.185, 0.18, 0.7, 0.025],                                           # Posición y Tamaño del Panel (LBWH)
            facecolor = '#3a3a3a'                                                    # Color de Fondo del Panel
                
        )
        self.slider: Slider = Slider(                                                  # Slider Interactivo para el Perímetro
                
            ax = self.slider_panel,                                                    # Panel donde se Ubica el Slider
            label = 'Perímetro (Mts)',                                                 # Etiqueta del Slider
            valmin = 1.0,                                                              # Valor Mínimo del Slider
            valmax = 100.0,                                                            # Valor Máximo del Slider
            valinit = 12.0,                                                            # Valor Inicial del Slider
            valstep = 0.1,                                                             # Paso de Incremento del Slider
            color = "#1280E7FF",                                                     # Color del Slider
            initcolor = '#666666',                                                   # Color Inicial del Slider

        )
        self.radio_panel: graphics.Axes = graphics.axes(                               # Panel para los Botones de Radio
                
            arg = [0.3, 0.304, 0.15, 0.10],                                            # Posición y Tamaño del Panel (LBWH)
            facecolor = '#2a2a2a'                                                    # Color de Fondo del Panel
                
        ) 
        self.radio = RadioButtons(                                                     # Botones de Radio para Modo de Visualización
                
            ax = self.radio_panel,                                                     # Panel donde se Ubican los Botones de Radio
            labels = ('Normal', 'Detallado', 'Técnico'),                               # Etiquetas de los Botones de Radio
            active = 0,                                                                # Botón Activo Inicial (Índice 0)
            activecolor = "#1280E7FF",                                               # Color del Botón Activo
            label_props = {'fontfamily': 'Times New Roman'}                            # Propiedades de Etiquetas de Botones de Radio

        )            
        self.perimeter: float = 12.0                                                   # Perímetro Inicial de la Ventana Normanda (Mts)
        self.norman_window_x: Optional[float] = None                                   # Ancho Óptimo de la Ventana Normanda (Mts)
        self.norman_window_y: Optional[float] = None                                   # Altura Óptima de la Ventana Normanda (Mts)
        self.max_area: Optional[float] = None                                          # Área Máxima Calculada de la Ventana Normanda (Mts^2)
        self.perimeters_record: list[float] = []                                       # Historial de Perímetros Calculados
        self.areas_record: list[float] = []                                            # Historial de Áreas Calculadas
        self.visualization_mode: Literal["Normal", "Detallado", "Técnico"] = 'Normal'  # Modo de Visualización Inicial  
        self.buttons: list[Button] = []                                                # Lista de Botones de la Ventana
        self.text_stats: list[Text] = []                                               # Estadísticas en Texto
        self._last_perimeter: Optional[float] = None                                   # Último Perímetro Calculado
        self._cached_dimensions: Optional[tuple[float, float, float]] = None           # Cache de Dimensiones Óptimas
        self._sensibility_cache_perimeters: Optional[numpy.ndarray] = None             # Caché de Perímetros Precalculados
        self._sensibility_cache_areas: Optional[numpy.ndarray] = None                  # Caché de Áreas Precalculadas

        # Configuraciones Finales
        self._configure_window_elements()                                              # Configurar Elementos de la Ventana                                                   
        self._configure_controls()                                                     # Configurar Controles
        
        # Actualizar Todo
        self._update_all()
        



    # Método Interno: Configurador de Elementos de la Ventana
    def _configure_window_elements(self) -> None:
        
        """
           - Método Interno: Configurador de Elementos de la Ventana
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Configurar Elementos Visuales de la Ventana
        """

        # Establecer Configuraciones para la Ventana Principal
        manager = graphics.get_current_fig_manager()                                  # Obtenemos el Administrador de la Ventana Actual
        BASE_DIR = Path(__file__).resolve().parent.parent                             # Directorio Base del Proyecto
        manager.window.setWindowIcon(QIcon(str(BASE_DIR/ "imgs" / "logo.ico")))       # Establecemos el Ícono Personalizado de la Ventana
        self.window.patch.set_facecolor("#000000")                                  # Color de Fondo de la Ventana Principal
        self.window.suptitle(                                                         # Título Principal de la Ventana Principal
                
            'Optimizador De Ventana Normanda',                                        # Texto del Título
            fontsize = 25, fontweight = 'bold', fontfamily = 'Times New Roman',       # Estilo de Fuente
            color = 'white',                                                          # Color del Texto
            y = 0.95                                                                  # Posición Vertical del Título 
                
        )                                                        
        self.window.text(                                                             # Subtítulo de la Ventana Principal
                
            0.5, 0.87,                                                                # Posición del Subtítulo 
            'Maximización de Área con Restricción de Perímetro',                      # Texto del Subtítulo
            ha = 'center',                                                            # Alineación Horizontal del Texto
            fontsize = 15, fontweight = 'bold', fontfamily = 'Times New Roman',       # Estilo de Fuente del Subtítulo
            color = 'white', style = 'italic'                                         # Color del Texto del Subtítulo

        )
            
        # Colores de Fondo Personalizados para los Paneles
        self.controls_panel.set_facecolor('#1a1a1a')                                # Panel de Controles
        self.normand_window_panel.set_facecolor('#0d1b2a')                          # Panel de Ventana Normanda
        self.area_graphic_panel.set_facecolor('#1b263b')                            # Panel de Gráfica Área vs Ancho
        self.results_panel.set_facecolor('#0d1b2a')                                 # Panel de Resultados
        self.sensibility_panel.set_facecolor('#1b263b')                             # Panel de Sensibilidad

        # Configuraciones Extras
        self.slider.label.set_fontfamily('Times New Roman')                           # Fuente Personalizada para el Slider
        self.results_panel.axis('off')                                                # Desactivar Ejes en el Panel de Resultados
 



    # Método Interno: Configurar Controles
    def _configure_controls(self) -> None:
        
        """
           - Método Interno: Configurador de Controles
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Configurar Controles de la Ventana
        """
        
        # Inicialización del Panel de Controles
        self.controls_panel.clear()                                                                                 # Limpieza Inicial
        self.controls_panel.set_xlim(0, 10)                                                                         # Límites Horizontales 
        self.controls_panel.set_ylim(0, 10)                                                                         # Límites Verticales 
        self.controls_panel.axis('off')                                                                             # Desactivar Ejes 
        
        # Ecuaciones del Problema
        self.controls_panel.text(                                                                                   # Texto: Modelo Matemático
        
            0.5, 9.5,                                                                                               # Posición del Texto 
            'Modelo Matemático',                                                                                    # Texto 
            fontsize = 13, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},                       # Estilo de Fuente
            color = 'white'                                                                                         # Color de Fuente
            
        )
        self.controls_panel.text(                                                                                   # Texto: Restricción de la Función
            
            0.3, 7.0,                                                                                               # Posición del Texto 
            r'Restricción: $P = x + 2y + \frac{\pi x}{2}$',                                                         # Texto
            fontsize = 11, fontdict = {'fontfamily': 'Times New Roman'}, color = '#ffd700'                        # Estilo de Fuente                        
            
        )
        self.controls_panel.text(                                                                                   # Texto: Objetivo de la Función
            
            0.3, 4.0,                                                                                               # Posición del Texto  
            r'Objetivo: $A = xy + \frac{\pi x^2}{8}$ → MAX',                                                        # Texto
            fontsize = 11, fontdict = {'fontfamily': 'Times New Roman'}, color = '#00ff00'                        # Estilo de Fuente
            
        )
        
        # Configuraciones Adicionales para el Texto del Slider
        self.slider.label.set_color('white')                                                                        # Color
        self.slider.label.set_fontweight('bold')                                                                    # Peso de Fuente
        self.slider.label.set_fontfamily('Times New Roman')                                                         # Tipo de Fuente

        # Configuraciones Adicionales para el Texto del Valor del Slider
        self.slider.valtext.set_color('#ffd700')                                                                  # Color
        self.slider.valtext.set_fontweight('bold')                                                                  # Peso de Fuente 
        self.slider.valtext.set_fontfamily('Times New Roman')                                                       # Tipo de Fuente
        self.slider.valtext.set_fontsize(11)                                                                        # Tamaño de Fuente

        # Asignar Función de Cambio al Slider
        self.slider.on_changed(lambda value: setattr(self, 'perimeter', value))                                     # Actualizar Perímetro al Cambiar el Slider
        self.window.canvas.mpl_connect('button_release_event', self._on_slider_release)                             # Evento al Soltar el Slider

        # Botones de Valores Predefinidos
        button_values = [5, 12, 25, 50, 100]                                                                        # Valores de Botón                            
        for i, value in enumerate(button_values):                                                                   # Recorrido de los Valores de Botones
            button_panel = graphics.axes([0.25 + i * 0.115, 0.1, 0.10, 0.04])                                       # Panel de Botón
            button = Button(                                                                                        # Botón 
                
                ax = button_panel,                                                                                  # Panel
                label = f'{value}Mts',                                                                              # Texto
                color = '#2a5a7a', hovercolor = '#3a7a9a'                                                       # Color, según Estado
                
            ) 
            button.label.set_color('white')                                                                         # Color de Fuente
            button.label.set_fontsize(9)                                                                            # Tamaño de Fuente
            button.label.set_fontweight('bold')                                                                     # Peso de Fuente
            button.label.set_fontfamily('Times New Roman')                                                          # Tipo de Fuente
            button.on_clicked(lambda event, value = value: (self.slider.set_val(value), self._update_all(event)))   # Accion de Click del Botón
            self.buttons.append(button)                                                                             # Añadimos el Botón a la Lista
        
        # Botones de Radio para Modo de Visualización
        for label in self.radio.labels:                                                                             # Recorrido de las Etiquetas
            label.set_color('white')                                                                                # Color de Fuente
            label.set_fontsize(9)                                                                                   # Tamaño de Fuente
            label.set_fontfamily('Times New Roman')                                                                 # Tipo de Fuente
        self.radio.on_clicked(self._change_visualization_mode)                                                      # En Click, nuevo Modo Visualización
        

  

    # Método Interno: Optimizar Dimensiones 
    def _optmize_dimensions(self, perimeter: Union[float, int]) -> tuple[Union[float, int], Union[float, int], Union[float, int]]:
        
        """
           - Método Interno: Optimizar Dimensiones 
           - Argumentos: 
                - perimeter (Union[float, int]): Perímetro de la Ventana Normanda
           - Retorno: Dimensiones Óptimas y Área Máxima (tuple[Union[float, int], Union[float, int], Union[float, int]])
           - Objetivo Principal: Configurar Controles de la Ventana
        """
        
        # Usar Caché si el Perímetro no Cambió
        not_needed_update = (                                                                                 # Condición de No Necesidad de Actualización
            
            self._last_perimeter is not None and                                                              # Hay un Perímetro Anterior
            abs(self._last_perimeter - perimeter) < 0.001 and                                                 # El Perímetro no Cambió Significativamente
            self._cached_dimensions is not None                                                               # Hay Dimensiones en Caché
            
        )  
        if not_needed_update: return self._cached_dimensions                                                  # Retornamos las Dimensiones en Caché
        
        # Ancho Máximo para la Ventana
        max_width = perimeter / (1 + numpy.pi / 2)


        # Función Interna: Área Negativa de la Ventana        
        def _negative_window_area(width: Union[float, int]) -> Union[float, int]:
        
            """
                - Función Interna: Área Negativa de la Ventana
                - Argumentos:
                        - width (Union[float, int]): Ancho de la Ventana
                - Retorno: Área Negativa de la Ventana (Union[float, int])
                - Objetivo Principal: Calcular Área Negativa de la Ventana para Optimización
            """
            
            # Cálculo de la Altura del Rectágulo
            height = (perimeter - width * (1 + numpy.pi / 2)) / 2

            # Si las Medidas son Negativas, lanzamos Error por Valor
            if height < 0 or width < 0: raise ValueError("Las Dimensiones de la Ventana son Inválidas")
            
            # Cálculo de las Aréas de las Figuras 
            rect_area = width * height                                                                      # Rectángulo
            semicircle_area = (numpy.pi * (width ** 2)) / 8                                                 # Semicírculo
            
            # Retornamos el Aréa Negativo Total de la Ventana Normanda
            return -(rect_area + semicircle_area)


        # Hallamos el Máximo de la Función Área mediante Optimización
        results = minimize_scalar(                                                                          # Busquéda
                
            fun = _negative_window_area,                                                                    # Función
            bounds = (0.01, max_width),                                                                     # Límites
            method = 'bounded'                                                                              # Métodos
                
        )

        # Cálculo de Dimensiones Óptimas y Área Máxima    
        optimus_width = results.x                                                                           # Ancho Óptimo                            
        optimus_height = (perimeter - optimus_width * (1 + numpy.pi / 2)) / 2                               # Alto Ótimo
        max_area = -results.fun                                                                             # Aréa Máxima
            
        # Guardar en Caché
        self._last_perimeter = perimeter                                                                    # Actualizamos el Último Perímetro
        self._cached_dimensions = (optimus_width, optimus_height, max_area)                                 # Guardamos las Dimensiones Óptimas en Caché

        # Retornamos los Resultados de la Optimización
        return (optimus_width, optimus_height, max_area)




    # Método Interno: Inicializar Caché de Sensibilidad
    def _initialize_sensibility_cache(self) -> None:
        
        """
            - Método Interno: Inicializar Caché de Sensibilidad
            - Argumentos: Ninguno
            - Retorno: Ninguno
            - Objetivo: Precalcular 100 Valores Exactos de Sensibilidad una sola vez
        """
        
        # Arrays de Perímetros y Áreas Precalculadas
        self._sensibility_cache_perimeters = numpy.linspace(1, 100, 100, dtype = numpy.float64)            # Perímetros de 1 a 100
        self._sensibility_cache_areas = numpy.empty(100, dtype = numpy.float64)                            # Array Vacío para Áreas
        
        # Calcular todas las Areas Máximas una sola vez
        for i, perimeter in enumerate(self._sensibility_cache_perimeters):                                 # Recorrido de Perímetros
            _, _, max_area = self._optmize_dimensions(perimeter)                                           # Optimizamos Dimensiones
            self._sensibility_cache_areas[i] = max_area                                                    # Guardamos el Área Máxima




    # Método Interno: Dibujar Ventana Normanda
    def _draw_normand_window(self) -> None:
        
        """
           - Método Interno: Dibujar Ventana Normanda
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Dibujar Ventana Normanda para su Visualización
        """
        
        # Limpieza Inicial del Panel
        self.normand_window_panel.clear()
        
        # Obtención de Datos de la Ventana
        width = self.norman_window_x                                                                # Ancho de la Ventana
        height = self.norman_window_y                                                               # Alto de la Ventana
        radio = width / 2                                                                           # Radio del Semicírculo de la Ventana
        
        # Título Dinámico según Modo
        titles = {
            
            'Normal': 'Ventana Normanda Optimizada',                                              
            'Detallado': 'Vista Detallada con Medidas',
            'Técnico': 'Especificaciones Técnicas'
        
        }
        
        # Agregar Título al Panel
        self.normand_window_panel.set_title(                                                       # Agregamos el Título
            
            titles[self.visualization_mode],                                                       # Título
            fontsize = 13, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'white', pad = 15                                                              # Color y Espacio   
            
        )
        
        # Dibujar Rectángulo con Degradado
        rects_num = 10 if self.visualization_mode == 'Detallado' else 1                            # Número de Rectángulos según Modo
        if rects_num > 1:                                                                          # Modo Detallado: Múltiples Figuras
            all_patches = [None] * (rects_num * 2)                                                 # Lista para todas las Figuras
            patch_index = 0                                                                        # Índice de la Figura Actual            
            for i in range(rects_num):                                                             # Crear todos los Rectángulos
                scale = 1 - (0.05 * i / rects_num)                                                 # Escala de Reducción
                scaled_width = width * scale                                                       # Ancho Escalado
                scaled_height = height * scale                                                     # Alto Escalado
                offset_x = (width - scaled_width) / 2                                              # Offset X para Centrado
                offset_y = (height - scaled_height) / 2                                            # Offset Y para Centrado
                all_patches[patch_index] = Rectangle(                                              # Crear Rectángulo
                    
                    xy = (offset_x, offset_y),                                                     # Posición 
                    width = scaled_width, height = scaled_height,                                  # Dimensiones
                    alpha = 0.3 + (0.4 * i / rects_num)                                            # Transparencia
                
                )
                patch_index += 1                                                                   # Incrementar Índice            
            for i in range(rects_num):                                                             # Crear todos los Semicírculos
                scale = 1 - (0.05 * i / rects_num)                                                 # Escala de Reducción
                radio_scaled = radio * scale                                                       # Radio Escalado
                all_patches[patch_index] = Wedge(                                                  # Crear Semicírculo

                    center = (width / 2, height),                                                  # Centro 
                    r = radio_scaled,                                                              # Radio
                    theta1 = 0, theta2 = 180,                                                      # Ángulo Inicial y Final
                    alpha = 0.3 + (0.4 * i / rects_num)                                            # Transparencia
                
                )
                patch_index += 1                                                                   # Incrementar Índice            
            collection = PatchCollection(                                                          # Colección de Parches
                
                all_patches,                                                                       # Iterable de Parches
                facecolors = '#4682b4', edgecolors = "#141618",                                # Colores
                linewidths = 2,                                                                    # Grosor de Borde
                alpha = 0.5,                                                                       # Transparencia
                zorder = 2                                                                         # Orden de Dibujo
            
            )
            self.normand_window_panel.add_collection(collection)                                   # Añadir Colección al Panel
        else:                                                                                      # Modo Normal: Una Sola Figura
            rect = Rectangle(                                                                      # Crear Rectángulo
                
                xy = (0, 0),                                                                       # Posición 
                width = width, height = height,                                                    # Dimensiones
                linewidth = 2,                                                                     # Grosor del Borde
                edgecolor = '#1e90ff', facecolor = '#4682b4',                                  # Colores
                alpha = 0.7,                                                                       # Transparencia
                zorder = 2                                                                         # Orden de Dibujo
            
            )
            semicircle = Wedge(                                                                    # Crear Semicírculo

                center = (width / 2, height),                                                      # Centro 
                r = radio,                                                                         # Radio
                theta1 = 0, theta2 = 180,                                                          # Ángulo Inicial y Final
                linewidth = 2,                                                                     # Grosor del Borde
                edgecolor = '#1e90ff', facecolor = '#4682b4',                                  # Colores
                alpha = 0.7,                                                                       # Transparencia
                zorder = 2                                                                         # Orden de Dibujo
            
            )
            self.normand_window_panel.add_patch(rect)                                              # Añadir Rectángulo al Panel
            self.normand_window_panel.add_patch(semicircle)                                        # Añadir Semicírculo al Panel
        
        # Líneas de División para Modo Detallado y Técnico
        if self.visualization_mode in frozenset(['Detallado', 'Técnico']):                         # Si el Modo es Detallado o Técnico
            for i in range(1, 4):                                                                  # Líneas Verticales
                self.normand_window_panel.plot(                                                    # Dibujar Línea
                    
                    [width * (i / 4), width * (i / 4)],                                            # Coordenadas X
                    [0, height],                                                                   # Coordenadas Y
                    'cyan',                                                                        # Color
                    linewidth = 1, linestyle='--',                                                 # Estilo de Línea
                    alpha = 0.3                                                                    # Transparencia
                
                )
            for i in range(1, 4):                                                                  # Líneas Horizontales
                self.normand_window_panel.plot(                                                    # Dibujar Línea
                    
                    [0, width],                                                                    # Coordenadas X
                    [height*( i / 4), height* (i / 4)],                                            # Coordenadas Y
                    'cyan',                                                                        # Color
                    linewidth = 1, linestyle = '--',                                               # Estilo de Línea
                    alpha = 0.3,                                                                   # Transparencia
                    
                )
        
        # Offsets para Anotaciones
        offset_x = -0.5                                                                            # Offset X para Anotaciones
        offset_y = -0.5                                                                            # Offset Y para Anotaciones

        # Anotación del Ancho
        self.normand_window_panel.annotate(                                                        # Anotación en Panel de Ventana Normanda
            
            text = '',                                                                             # Texto Vacío
            xy = (width, offset_x + 0.25),                                                         # Coordenadas Finales     
            xytext = (0, offset_x + 0.25),                                                         # Coordenadas Iniciales 
            arrowprops = dict(                                                                     # Propiedades de la Flecha
                
                arrowstyle = '<->',                                                                # Estilo de Flecha 
                lw = 2,                                                                            # Grosor de la Línea
                color = 'yellow',                                                                  # Color de la Flecha
                mutation_scale = 20                                                                # Escala de la Flecha
                
            )
            
        )
        x_text = self.normand_window_panel.text(                                                   # Texto de la Dimensión X
        
            width / 2, offset_x - 0.3,                                                             # Posición del Texto 
            f'x = {width:.4f} Mts',                                                                # Texto
            ha = 'center',                                                                         # Alineación Horizontal
            fontsize = 12, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'black',                                                                       # Color
            bbox = dict(                                                                           # Propiedades del Cuadro de Texto
                
                boxstyle = 'round,pad=0.7',                                                        # Estilo de Caja
                facecolor = '#ffcc00', edgecolor = 'orange',                                     # Colores
                linewidth = 2.5,                                                                   # Grosor del Borde
                alpha = 0.95                                                                       # Transparencia

            )

        )
        x_text.set_path_effects([fig_effects.withStroke(linewidth = 2, foreground = 'white')])     # Efecto de Borde
        
        # Anotación de la Altura
        self.normand_window_panel.annotate(                                                        # Anotación en Panel de Ventana Normanda
            
            text = '',                                                                             # Texto Vacío
            xy = (offset_y + 0.25, height),                                                        # Coordenadas Finales 
            xytext = (offset_y + 0.25, 0),                                                         # Coordenadas Iniciales 
            arrowprops = dict(                                                                     # Propiedades de la Flecha
                 
                arrowstyle = '<->',                                                                # Estilo de Flecha
                lw = 2,                                                                            # Grosor de la Línea
                color = 'lime',                                                                    # Color de la Flecha
                mutation_scale = 20                                                                # Escala de la Flecha

            )
            
        )
        y_text = self.normand_window_panel.text(                                                   # Texto de la Dimensión Y
            
            offset_y - 0.4, height / 2,                                                            # Posición del Texto 
            f'y = {height:.4f} Mts',                                                               # Texto
            ha = 'center',                                                                         # Alineación Horizontal
            rotation = 90,                                                                         # Rotación del Texto
            fontsize = 12, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'black',                                                                       # Color del Texto
            bbox = dict(                                                                           # Propiedades del Cuadro de Texto

                boxstyle = 'round,pad=0.7',                                                        # Estilo de Caja
                facecolor = '#00ff00', edgecolor = 'darkgreen',                                  # Colores
                linewidth = 2.5,                                                                   # Grosor del Borde    
                alpha = 0.95                                                                       # Transparencia
                
            )
         
        )
        y_text.set_path_effects([fig_effects.withStroke(linewidth = 2, foreground = 'white')])     # Efecto de Borde
        
        # Radio
        angle = numpy.pi / 3                                                                       # Ángulo para la Línea del Radio
        self.normand_window_panel.plot(                                                            # Línea del Radio
            
            [width/2, (width / 2) + (radio * numpy.cos(angle))],                                   # Coordenadas X
            [height, (height + radio) * numpy.sin(angle)],                                         # Coordenadas Y
            'red',                                                                                 # Color de la Línea 
            linewidth = 3.5,                                                                       # Grosor de la Línea
            zorder = 5                                                                             # Orden de Dibujo
            
         )
        self.normand_window_panel.plot(                                                            # Punto Final del Radio
            
            width / 2,                                                                             # Coordenada X
            height,                                                                                # Coordenada Y 
            'o',                                                                                   # Marcador
            color = 'red',                                                                         # Color del Marcador
            markersize = 10, markeredgecolor = 'white', markeredgewidth = 2,                       # Estilo del Marcador
            zorder = 6                                                                             # Orden de Dibujo
            
        )        
        radio_text = self.normand_window_panel.text(                                               # Texto del Radio
        
            0.525,                                                                                 # Posición X del Texto
            0.95,                                                                                  # Posición Y del Texto
            f'r = {radio:.4f} Mts',                                                                # Texto
            transform = self.normand_window_panel.transAxes,                                       # Transformación de Coordenadas
            ha = 'center', va = 'top',                                                             # Alineación 
            fontsize = 11, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'black',                                                                       # Color
            bbox = dict(                                                                           # Propiedades del Cuadro de Texto
                
                boxstyle = 'round,pad=0.7',                                                        # Estilo de Caja
                facecolor = '#ff6347', edgecolor = 'darkred',                                    # Colores
                linewidth = 2.5,                                                                   # Grosor del Borde
                alpha = 0.95                                                                       # Transparencia
                
            )
            
        )
        radio_text.set_path_effects([fig_effects.withStroke(linewidth = 2, foreground = 'white')]) # Efecto de Borde
        
        # Información Adicional en Modo Técnico                                           
        if self.visualization_mode == 'Técnico':                                                   # Si el Modo es Técnico
            info_tec = f'Área Rectángulo: {width * height:.4f} Mts²\n'                             # Área del Rectángulo          
            info_tec += f'Área Semicírculo: {(numpy.pi * (radio ** 2)):.4f} Mts²\n'                # Área del Semicírculo
            info_tec += f'Perímetro Real: {(width + 2) * (height + (numpy.pi * radio)):.4f} Mts'   # Perímetro Real  
            self.normand_window_panel.text(                                                        # Texto de Información Técnica
                
                0.8, 0.95,                                                                         # Posición del Texto 
                info_tec,                                                                          # Texto
                transform = self.normand_window_panel.transAxes,                                   # Transformación de Coordenadas
                fontsize = 7, color = 'cyan', fontdict = {'fontfamily': 'Times New Roman'},        # Estilo de Fuente
                verticalalignment = 'top',                                                         # Alineación Vertical
                bbox = dict(                                                                       # Propiedades del Cuadro de Texto               
                    
                    boxstyle = 'round',                                                            # Estilo de Caja
                    facecolor = 'black', edgecolor = 'cyan',                                       # Colores
                    alpha = 0.7                                                                    # Transparencia
                    
                )
                
            )
        
        # Configuración de Ejes
        margin = 1.2                                                                               # Margen Extra
        self.normand_window_panel.set_xlim(-1.5, width + margin)                                   # Límites X
        self.normand_window_panel.set_ylim(-1.2, height + radio + margin)                          # Límites Y
        self.normand_window_panel.set_aspect('equal')                                              # Aspecto Igual
        self.normand_window_panel.grid(                                                            # Configuración de la Cuadrícula            
            
            visible = True,                                                                        # Visibilidad
            alpha = 0.2,                                                                           # Transparencia
            linestyle = ':',                                                                       # Estilo de Línea
            color = 'white'                                                                        # Color de la Línea
            
        )
        self.normand_window_panel.set_xlabel(                                                      # Etiqueta Eje X
            
            'Ancho (Mts)',                                                                         # Texto de la Etiqueta
            fontsize = 11, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'white'                                                                        # Color del Texto
            
        )
        self.normand_window_panel.set_ylabel(                                                      # Etiqueta Eje Y
             
            'Altura (Mts)',                                                                        # Texto de la Etiqueta
            fontsize = 11, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},      # Estilo de Fuente
            color = 'white'                                                                        # Color del Texto
        
        )
        self.normand_window_panel.tick_params(colors = 'white')                                    # Color de las Marcas de los Ejes
        self.normand_window_panel.set_facecolor('#0d1b2a')                                       # Color de Fondo del Panel
        



    # Método Interno: Graficar Aréa vs Ancho
    def _graph_area_vs_width(self) -> None:
        
        """
           - Método Interno: Graficar Aréa vs Ancho
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Graficar los Cambios del Area cuando el Ancho cambia
        """
        
        # Limpieza Inicial del Panel
        self.area_graphic_panel.clear()
        
        # Obtención de Datos
        max_width = (self.perimeter / (1 + (numpy.pi / 2)))                                    # Valor Máximo del Ancho del Rectángulo
        width_values = numpy.linspace(0.01, max_width, 150)                                    # Generar 150 Valores de Ancho 
        heights = (self.perimeter - width_values * (1 + (numpy.pi / 2))) / 2                   # Calcular Alturas Correspondientes
        areas = numpy.where(                                                                   # Calcular Áreas Correspondientes
            
            heights > 0,                                                                       # Condición para Alturas Válidas
            (width_values * heights) + (numpy.pi * (width_values ** 2)) / 8,                   # Cálculo de Áreas Válidas
            0                                                                                  # Áreas Inválidas (Alturas Negativas
        
        )
            
        # Dibujar la Gráfica
        self.area_graphic_panel.plot(                                                          # Dibujar Línea                                                 
            
            width_values,                                                                      # Coordenada X
            areas,                                                                             # Coordenada Y
            'cyan',                                                                            # Color
            linewidth = 3,                                                                     # Ancho de Línea
            label = 'A(x)',                                                                    # Texto
            alpha = 0.8,                                                                       # Opacidad

        )
        self.area_graphic_panel.fill_between(                                                  # Rellenar de un Color una Sección
            
            width_values, areas,                                                               # Posición  
            alpha = 0.3,                                                                       # Opacidad
            color = 'cyan'                                                                     # Color
        
        )
        self.area_graphic_panel.plot(                                                          # Dibujar Línea
            
            self.norman_window_x,                                                              # Coordenada x
            self.max_area,                                                                     # Coordenada Y
            'o', markersize = 15, markeredgecolor = 'red', markeredgewidth = 3,                # Estilo del Marcador
            color = 'yellow',                                                                  # Color
            label = 'Máximo',                                                                  # Texto
            zorder = 10                                                                        # Orden de Dibujado
            
        )        
        self.area_graphic_panel.axvline(                                                       # Línea de Referencia Vertical
            
            self.norman_window_x,                                                              # Coordenada X
            color = 'yellow',                                                                  # Color
            linestyle = '--', linewidth = 2,                                                   # Estilo de Línea
            alpha = 0.6                                                                        # Opacidad
            
        )
        self.area_graphic_panel.axhline(                                                       # Línea de Referencia Horizontal
            
            self.max_area,                                                                     # Coordenada X
            color = 'yellow',                                                                  # Color
            linestyle = '--', linewidth = 2,                                                   # Estilo de Línea
            alpha = 0.6                                                                        # Opacidad
            
        )        
        self.area_graphic_panel.annotate(                                                      # Anotación del Máximo
            
            text = f'MAX\n({self.norman_window_x:.2f}, {self.max_area:.2f})',                  # Texto
            fontfamily = 'Times New Roman', fontsize = 10, fontweight = 'bold',                # Estilo de Fuente
            xy = (self.norman_window_x, self.max_area),                                        # Posición de Anotación
            xytext = (20.1, 20.1),                                                             # Posición de Texto
            textcoords = 'offset points',                                                      # Sistema de Coordenadas del Texto
            multialignment = 'center',                                                         # Alineación Múltiple
            bbox = dict(                                                                       # Propiedades del Cuadro de Texto
                
                boxstyle = 'round,pad=0.5',                                                    # Estilo de Caja 
                facecolor = 'yellow', edgecolor = 'red',                                       # Colores     
                linewidth = 2                                                                  # Borde de Línea
                
            ),
            arrowprops = dict(                                                                 # Propiedades de Flecha
                
                arrowstyle = '->',                                                             # Estilo  
                connectionstyle = 'arc3,rad=0.3',                                              # Estilo de Conexión
                color = 'red',                                                                 # Color
                lw = 2                                                                         # Grosor de Línea
                
            )
        
        )
        self.area_graphic_panel.set_xlabel(                                                    # Etiqueta de Dimensión X
            
            'Ancho (Mts)',                                                                     # Texto
            fontsize = 10, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},  # Estilo de Fuente
            color = 'white'                                                                    # Color
            
        )
        self.area_graphic_panel.set_ylabel(                                                    # Etiqueta de Dimensión Y
            
            'Área (Mts²)',                                                                     # Texto
            fontsize = 10, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},  # Estilo de Fuente
            color = 'white'                                                                    # Color
            
        )
        self.area_graphic_panel.set_title(                                                     # Título
            
            'Función Área Vs Ancho',                                                           # Texto
            fontsize = 11, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},  # Estilo de Fuente 
            color = 'white'                                                                    # Color
            
        )
        self.area_graphic_panel.legend(                                                        # Leyenda de la Gráfica
            
            loc = 'upper right',                                                               # Ubicación 
            bbox_to_anchor = (1.2, 0.67),                                                      # Posición de Caja 
            fontsize = 9,                                                                      # Tamaño de Fuente
            facecolor = '#1a1a1a', edgecolor = 'cyan', labelcolor = 'white'                  # Colores
            
        )
        self.area_graphic_panel.grid(                                                          # Cuadrícula de la Gráfica
            
            visible = True,                                                                    # Visible
            alpha = 0.3,                                                                       # Opacidad
            linestyle = ':', color = 'white'                                                   # Estilo de Línea
            
        )
        self.area_graphic_panel.tick_params(colors = 'white')                                  # Aplicamos Color a Diferentes Elementos

        


    # Método Interno: Mostrar Resultados Detallados
    def _see_results(self) -> None:
       
        """
           - Método Interno: Mostrar Resultados Detallados
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Mostrar Resultados Detallados en el Panel de Resultados
        """
                
        # Configuraciones Iniciales
        self.results_panel.clear()                                                                       # Limpieza Inicial
        self.results_panel.set_xlim(0, 10)                                                               # Límites en X
        self.results_panel.set_ylim(0, 10)                                                               # Límites en Y
        self.results_panel.axis('off')                                                                   # Desactivar Ejes
        
        # Estadísticas en Tiempo Real
        self.results_panel.text(                                                                         # Agregar Texto al Panel
            
            1.5, 9.5,                                                                                    # Posición del Texto
            'Estadísticas en Tiempo Real',                                                               # Texto
            fontsize = 13, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},            # Estilo de Fuente
            color = 'white'                                                                              # Color
            
        )

        # Obtención de Datos
        results = [                                                                                      # Resultados
                     
            ('Entrada de Datos', ''),                                                                    # Entrada del Usuario
            (f'Perímetro:', f'{self.perimeter:.4f} Mts', 'cyan'),                                        # Perímetro
            ('Dimensiones Óptimas', ''),                                                                 # Dimensiones Calculadas
            (f'Ancho (x):', f'{self.norman_window_x:.4f} m', '#00ff00'),                               # Ancho
            (f'Altura (y):', f'{self.norman_window_y:.4f} m', '#00ff00'),                              # Altura
            (f'Radio (r):', f'{(self.norman_window_x / 2):.4f} m', '#00ff00'),                         # Radio
            ('Áreas Parciales', ''),                                                                     # Areas por figura
            (f'Rectángulo:', f'{self.norman_window_x*self.norman_window_y:.4f} m²', 'yellow'),           # Rectángulo
            (f'Semicírculo:', f'{(numpy.pi * ((self.norman_window_x/2) ** 2)):.4f} m²', 'yellow'),       # Semícirculo
        
        ]
        label_positions = [7.5, 5.5, 4.5, 3.5, 1.5, 0.5]                                                 # Posiciones Y de las Etiquetas
        headers_positions = [(3.3, 8.5), (3.0, 6.5), (3.6, 2.5)]                                         # Posiciones de los Encabezados
        headers_index = 0                                                                                # Índice de Encabezados
        labels_index = 0                                                                                 # Índice de Etiquetas

        # Dibujar Resultados
        for item in results:                                                                             # Recorrido de Datos
            if len(item) == 2:                                                                           # Si el Dato solo tiene 2 Valores
                label, value = item                                                                      # Asignar Valores                                            
                color = 'white'                                                                          # Color por Defecto
            else: label, value, color = item                                                             # Asignar Valores ya Definidos
            if label.startswith('Dim') or label.startswith('Ent') or label.startswith('Áre'):            # Si es el Encabezado
                self.results_panel.text(                                                                 # Encabezado
                    
                    headers_positions[headers_index][0], headers_positions[headers_index][1],            # Posición 
                    label,                                                                               # Texto
                    fontsize = 10, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},    # Estilo de Fuente
                    color = color                                                                        # Color
                     
                )
                headers_index += 1                                                                       # Actualizar Indica
            else:                                                                                        # Si es un Dato Normal
                self.results_panel.text(                                                                 # Dato                        

                    1.5, label_positions[labels_index],                                                  # Posición 
                    label,                                                                               # Texto
                    fontsize = 9, fontdict = {'fontfamily': 'Times New Roman'}, color = 'white'          # Estilo de Fuente
                    
                )
                if value:                                                                                # Si hay Valor de Dato
                    self.results_panel.text(                                                             # Dibujamos Valor de Dato
                        
                        8.5, label_positions[labels_index],                                              # Posición 
                        value,                                                                           # Texto
                        fontsize = 9, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'}, # Estilo de Fuente
                        color = color,                                                                   # Color
                        ha = 'right'                                                                     # Alíneado
                                          
                    )
                labels_index += 1                                                                        # Actualizar Indice

    


    # Método Interno: Mostrar Resultados Detallados
    def _graph_sensibility(self) -> None:

        """
           - Método Interno: Graficar Análisis de Sensibilidad
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Graficar el Análisis de Sensibilidad del Área Máxima vs Perímetro
        """        
        
        # Limpieza Inicial del Panel
        self.sensibility_panel.clear()
        
        # Inicializar Caché solo la primera vez
        if self._sensibility_cache_perimeters is None: self._initialize_sensibility_cache()
        
        # Usar Datos Precalculados
        perimeters = self._sensibility_cache_perimeters                                         # Perímetros 
        max_areas = self._sensibility_cache_areas                                               # Áreas Máximas Correspondientes  
        
        # Graficar
        self.sensibility_panel.plot(                                                            # Línea de Área Máxima vs Perímetro
            
            perimeters, max_areas,                                                              # Posición 
            'lime',                                                                             # Color
            linewidth = 2.5,                                                                    # Grosor de Línea
            label = 'Área Máxima',                                                              # Texto
            
        )
        self.sensibility_panel.fill_between(                                                    # Relleno de Color
            
            perimeters, max_areas,                                                              # Posición 
            alpha = 0.3,                                                                        # Opacidad
            color = 'lime'                                                                      # Color
            
        )        
        self.sensibility_panel.plot(                                                            # Valor Actual
               
            self.perimeter, self.max_area,                                                      # Posición 
            'o',                                                                                # Marcador                  
            color = 'red',                                                                      # Color
            markersize = 12, markeredgecolor = 'yellow', markeredgewidth = 2,                   # Estilo de Marcador
            label = 'Actual',                                                                   # Texto    
            zorder = 10                                                                         # Orden de Dibujado
            
        )
        self.sensibility_panel.axvline(                                                         # Línea Vertical
             
            self.perimeter,                                                                     # Posición X 
            color = 'red', linestyle='--',                                                      # Estilo de Línea
            alpha = 0.5                                                                         # Opacidad
            
        )
        self.sensibility_panel.set_xlabel(                                                      # Etiqueta Vertical
            
            'Perímetro (Mts)',                                                                  # Texto
            fontsize = 10, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},   # Estilo de Fuente
            color = 'white'                                                                     # Color
            
        )
        self.sensibility_panel.set_ylabel(                                                      # Etiqueta Horizontal
            
            'Área Máxima (Mts²)',                                                               # Texto
            fontsize = 10, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},   # Estilo de Fuente
            color = 'white'                                                                     # Color
            
        )
        self.sensibility_panel.set_title(                                                       # Título
             
            'Análisis de Sensibilidad',                                                         # Texto
            fontsize = 11, fontweight = 'bold', fontdict = {'fontfamily': 'Times New Roman'},   # Estilo de Fuente
            color = 'white'                                                                     # Color
            
        )
        self.sensibility_panel.legend(                                                          # Leyenda
            
            loc = 'upper left',                                                                 # Ubicación
            fontsize = 9,                                                                       # Tamaño de Fuente
            facecolor =  '#1a1a1a', edgecolor = 'cyan', labelcolor = 'white'                  # Colores
            
        )
        self.sensibility_panel.grid(                                                            # Cuadrícula
            
            visible = True,                                                                     # Visible
            alpha = 0.3,                                                                        # Opacidad
            linestyle = ':', color = 'white'                                                    # Estilo de Línea
            
        )
        self.sensibility_panel.tick_params(colors = 'white')                                    # Elementos de Color Blanco
    
    
    

    # Método Interno: Actualizar Estadísticas
    def _update_stats(self) -> None:
        
        """
           - Método Interno: Actualizar Estadísticas
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Actualizar las Estadísticas en Tiempo Real
        """         
        
        # Actualizar Estadísticas
        if len(self.perimeters_record) > 0:                                                              # Si hay Registro de Perímetros
            stats_texts = [                                                                              # Obtener las Estadísticas
                
                f'Cálculos Realizados: {len(self.perimeters_record)}',
                f'Perímetro Promedio: {numpy.mean(self.perimeters_record):.2f} Mts',
                f'Área Promedio: {numpy.mean(self.areas_record):.2f} Mts²',
                f'Mayor Área Encontrada: {numpy.max(self.areas_record):.2f} Mts²'
            
            ]
            for text_obj, new_text in zip(self.text_stats, stats_texts): text_obj.set_text(new_text)     # Agregar Texto a la Lista
    



    # Método Interno: 
    def _update_all(self, event = None) -> None:

        """
           - Método Interno: Actualizar Estadísticas
           - Argumentos:
                - event: Evento de Actualización (Opcional)
           - Retorno: Ninguno
           - Objetivo Principal: Actualizar las Estadísticas en Tiempo Real
        """  

        # Calcular Dimensiones Óptimas
        self.norman_window_x, self.norman_window_y, self.max_area = self._optmize_dimensions(self.perimeter)
            
        # Agregar al Historial
        self.perimeters_record.append(self.perimeter)                                                            # Perímetros
        self.areas_record.append(self.max_area)                                                                  # Areas
            
        # Limitar Tamaño del Historial
        if len(self.perimeters_record) > 20:                                                                     # Si excede a 20 Elementos
            self.perimeters_record.pop(0)                                                                        # Eliminar el Ultimo de Perímetros
            self.areas_record.pop(0)                                                                             # Elimianr el Ultimo de Areas
            
        # Actualizar todas las Visualizaciones
        self._draw_normand_window()                                                                              # Ventana Normanda
        self._graph_area_vs_width()                                                                              # Gráfica de Area Vs Ancho
        self._see_results()                                                                                      # Resultados
        self._graph_sensibility()                                                                                # Gráfica de Sensibilidad
        self._update_stats()                                                                                     # Actualizar Estadísticas
    
        # Redibujar la Ventana
        self.window.canvas.draw_idle()


    

    # Método Interno: Evento al Soltar el Mouse en el Slider
    def _on_slider_release(self, event) -> None:
        
        """
            - Método Interno: Manejar Evento de Soltar Mouse
            - Argumentos: 
                - event: Evento de Mouse
            - Retorno: Ninguno
            - Objetivo Principal: Actualizar Solo cuando el Usuario Suelta el Slider
        """
        
        # Actualizar Solo si el Evento Ocurre en el Slider
        if event.inaxes == self.slider_panel:                       # Si el Evento Ocurre en el Panel del Slider
            self.perimeter = self.slider.val                        # Actualizar el Perímetro
            self._update_all()                                      # Actualizar Todo        




    # Método Interno: Cambiar Modo de Visualización
    def _change_visualization_mode(self, mode: str) -> None:
        
        """
           - Método Interno: Cambiar Modo de Visualización
           - Argumentos: Ninguno
           - Retorno: Ninguno
           - Objetivo Principal: Cambiar Modo de Visualización para la Ventana Normanda
        """
        
        # Cambios 
        self.visualization_mode = mode    # Modo de Visualización
        self._draw_normand_window()       # Dibujamos Ventana Normanda
        self.window.canvas.draw_idle()    # Dibujamos de Nuevo toda la Ventana

# ----------------------------------------------------------------------------------------------------------------------------------------
