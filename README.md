# 🔷 GeoFrame - Optimizador de Ventana Normanda

**Aplicación interactiva para calcular y visualizar las dimensiones óptimas de ventanas normandas**

---

## 📑 Tabla de Contenidos

- [📖 Descripción del Proyecto](#-descripción-del-proyecto)
- [🎯 Problema Matemático](#-problema-matemático)
- [📐 Fundamento Matemático](#-fundamento-matemático)
- [⚡ Características](#-características)
- [🔧 Implementación Técnica](#-implementación-técnica)
- [💾 Instalación](#-instalación)
- [🖥️ Configuración de Pantalla](#️-configuración-de-pantalla)
- [🚀 Uso](#-uso)
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [🎓 Contexto Académico](#-contexto-académico)
- [📜 Licencia](#-licencia)
- [👤 Autor](#-autor)

---

## 📖 Descripción del Proyecto

**GeoFrame** es una aplicación científica desarrollada en Python que resuelve un clásico **problema de optimización con restricciones**: encontrar las dimensiones óptimas de una ventana normanda que **maximicen su área** dado un **perímetro fijo**.

Este proyecto fue concebido como una herramienta educativa para visualizar y comprender conceptos matemáticos como la optimización, las derivadas y las aplicaciones prácticas del cálculo en el diseño arquitectónico.

### 🏛️ ¿Qué es una Ventana Normanda?

Una **ventana normanda** (también conocida como ventana semicircular o ventana románica) es una estructura arquitectónica compuesta por:
- Un **rectángulo** con base `x` y altura `y`
- Un **semicírculo** con radio `r = x/2` colocado sobre la base del rectángulo

Este clásico diseño arquitectónico combina estabilidad estructural con estética, y presenta un interesante desafío matemático: **¿Cómo distribuir un perímetro limitado para obtener la máxima área posible?**

---

## 🎯 Problema Matemático

### 💡 El Desafío

Imagina que tienes un marco de ventana con un perímetro fijo `P` (por ejemplo, 12 metros de material). ¿Cómo debes diseñar la ventana para que entre la **mayor cantidad de luz** (área) posible?

Este no es un problema intuitivo porque:
- Si la ventana es demasiado ancha, la altura disminuye
- Si es demasiado alta, el ancho y el semicírculo se reducen
- El equilibrio óptimo requiere cálculo y técnicas de optimización


---

## 📐 Fundamento Matemático

### 1️⃣ Ecuación de Restricción (Perímetro)

El perímetro de una ventana normanda se compone de:
- Base del rectángulo: `x`
- Dos lados verticales: `2y`
- Semicircunferencia superior: `πr = π(x/2)`

**Restricción de perímetro:**
```
P = x + 2y + πx/2
P = x(1 + π/2) + 2y
```

Despejando `y`:
```
y = (P - x(1 + π/2)) / 2
```

### 2️⃣ Función Objetivo (Área)

El área total es la suma de:
- Área del rectángulo: `A_rect = xy`
- Área del semicírculo: `A_semi = πr²/2 = π(x/2)²/2 = πx²/8`

**Función de área total:**
```
A(x) = xy + πx²/8
```

Sustituyendo `y` de la restricción:
```
A(x) = x · [(P - x(1 + π/2))/2] + πx²/8
A(x) = (Px)/2 - x²(1 + π/2)/2 + πx²/8
A(x) = (Px)/2 - x²/2 - πx²/4 + πx²/8
A(x) = (Px)/2 - x²/2 - πx²/8
```

### 3️⃣ Optimización (Encontrando el Máximo)

Para encontrar el máximo, tomamos la derivada e igualamos a cero:

```
dA/dx = P/2 - x - πx/4 = 0
P/2 = x(1 + π/4)
x_óptimo = P / (2 + π/2)
```

Una vez obtenido `x_óptimo`, calculamos:
```
y_óptimo = (P - x_óptimo(1 + π/2)) / 2
A_máx = x_óptimo · y_óptimo + π(x_óptimo)²/8
```

### 4️⃣ Verificación (Prueba de la Segunda Derivada)

Para confirmar que es un máximo (y no un mínimo):
```
d²A/dx² = -1 - π/4 < 0  ✓ (Confirma que es un máximo)
```

---

## ⚡ Características

### 🎮 Funcionalidad Principal
- **Optimización automática:** Calcula las dimensiones óptimas (x, y, r) mediante métodos numéricos avanzados (SciPy)
- **Actualizaciones en tiempo real:** Todas las visualizaciones se actualizan dinámicamente al cambiar el perímetro
- **Slider interactivo:** Ajusta el perímetro de 1 a 100 metros con precisión de 0.1
- **Valores predeterminados rápidos:** Botones para valores comunes (5, 12, 25, 50, 100 metros)

### 📊 Paneles de Visualización

**1. 🖼️ Panel de Ventana Normanda**
- Representación geométrica interactiva
- Dimensiones anotadas con flechas
- Tres modos de visualización:
  - **Normal:** Vista limpia y básica
  - **Detallado:** Líneas de cuadrícula y múltiples capas
  - **Técnico:** Especificaciones completas con áreas parciales

**2. 📈 Gráfica de Área vs Ancho**
- Curva de la función de área A(x)
- Identificación visual del punto máximo
- Líneas de referencia hacia las dimensiones óptimas
- Anotación dinámica con coordenadas

**3. 📋 Panel de Resultados Numéricos**
- Visualización de datos de entrada
- Dimensiones óptimas (x, y, r)
- Áreas parciales (rectángulo y semicírculo)
- Todos los valores con precisión de 4 decimales

**4. 🔍 Gráfica de Análisis de Sensibilidad**
- Muestra cómo varía el área máxima con el perímetro
- Rango de 1 a 100 metros
- Resaltado del punto actual
- Útil para análisis de escenarios hipotéticos

### ⚙️ Optimizaciones de Rendimiento

- **Caché inteligente:** Almacena resultados calculados previamente para evitar cómputos redundantes
- **Precálculo:** Los datos de sensibilidad se calculan una vez y se reutilizan
- **Gestión de historial:** Mantiene un registro de los últimos 20 cálculos

---

## 🔧 Implementación Técnica

### 🛠️ Tecnologías Utilizadas

**Bibliotecas Principales:**
- **Python 3.11:** Lenguaje de programación principal
- **Matplotlib 3.5+:** Graficación y visualización avanzada
- **PyQt5:** Interfaz gráfica de usuario y gestión de ventanas
- **NumPy:** Cómputo numérico y operaciones con arreglos
- **SciPy:** Algoritmos avanzados de optimización (`minimize_scalar`)
- **Seaborn:** Estilizado profesional para gráficas


### 🏗️ Arquitectura

La aplicación sigue los principios de la **Programación Orientada a Objetos**:
- **Clase `GeoFrame`:** Controlador principal de la aplicación
- **Separación de responsabilidades:** Cada panel tiene su propio método de actualización
- **Diseño orientado a eventos:** Responde a interacciones del usuario (slider, botones, botones de radio)
- **Estructura modular:** Fácil de mantener y extender

---
## 💾 Instalación

**¡No requiere instalación ni dependencias!** El juego está disponible como ejecutable listo para usar.

### 📥 Descarga y Ejecución

1. Ve a la sección de [Releases](https://github.com/TheNarratorVIMXXX/GeoFrame/releases)
2. Descarga el archivo `GeoFrame.exe`
3. Haz doble clic para ejecutar
4. ¡Listo!

> ⚠️ **Nota:** No es necesario tener Python instalado ni configurar ningún entorno.

---

## 🖥️ Configuración de Pantalla

### 📺 Configuración Recomendada para Visualización Óptima

Para la mejor experiencia visual con **GeoFrame**, recomendamos la siguiente configuración de pantalla:

#### **Resolución de Pantalla**
- **Recomendada:** 1920 × 1080 (Full HD)
- Esta resolución garantiza que todos los paneles, gráficas y controles se muestren correctamente sin superponerse

#### **Escala y Diseño (Windows)**
La interfaz de la aplicación está optimizada para dos niveles de zoom específicos:

**Opción 1: Escala al 150% (Recomendada)**
- Mejor equilibrio entre visibilidad y espacio en pantalla
- Texto y controles cómodos de leer
- Las gráficas mantienen proporciones óptimas

**Opción 2: Escala al 100%**
- Máximo aprovechamiento de la pantalla
- Todos los paneles visibles simultáneamente
- Recomendada para sesiones de análisis detallado

#### **Cómo Ajustar la Configuración de Pantalla (Windows 10/11)**

1. Haz clic derecho en el escritorio y selecciona **Configuración de pantalla**
2. En **Escala y diseño**, busca el menú desplegable de **Resolución de pantalla**
   - Establece en **1920 × 1080 (Recomendado)**
3. En la misma sección, busca el menú desplegable de **Escala**
   - Elige **100%** o **150%** según tu preferencia
4. Haz clic en **Aplicar** y reinicia la aplicación GeoFrame

#### ⚠️ Notas Importantes

- **Otras resoluciones:** La aplicación funcionará en otras resoluciones, pero el diseño puede no ser óptimo
- **Otras escalas:** Usar escalas como 125% o 175% puede causar problemas menores de alineación
- **Múltiples monitores:** Si usas varios monitores, asegúrate de que GeoFrame se ejecute en el monitor con la configuración recomendada

---

## 🚀 Uso

### 🎯 Operación Básica

1. **Abre la aplicación:** Haz doble clic para ejecutar la aplicación
2. **Ajusta el perímetro:** Usa el slider interactivo o los botones predeterminados
3. **Observa los resultados:** Todos los paneles se actualizan automáticamente
4. **Cambia el modo de visualización:** Usa los botones de radio (Normal/Detallado/Técnico)
5. **Analiza la sensibilidad:** Observa cómo cambia el área con diferentes perímetros

### 📊 Interpretación de Resultados

**Ejemplo con P = 12 metros:**
```
Ancho Óptimo (x):       4.2667 m
Altura Óptima (y):      1.6234 m
Radio del Semicírculo:  2.1333 m
Área Máxima:           13.5752 m²
```

Esto significa que con 12 metros de perímetro, el diseño que permite la mayor entrada de luz es una ventana de 4.27 metros de ancho y 1.62 metros de alto, con un área total de 13.58 metros cuadrados.

---

## 📜 Licencia

# LICENCIA DE SOFTWARE PROPIETARIO
**Copyright © 2025 Carlos Gabriel Magallanes López**  
**Todos los Derechos Reservados**

---

## OTORGAMIENTO DE LICENCIA

Esta licencia te permite:

✅ Descargar y usar el software con fines personales y educativos  
✅ Instalar y ejecutar la aplicación en tus dispositivos personales

---

## RESTRICCIONES

**NO** puedes:

❌ Modificar, aplicar ingeniería inversa, descompilar o desensamblar el software  
❌ Redistribuir, compartir o poner copias a disposición de otros  
❌ Usar el software con fines comerciales sin permiso escrito  
❌ Eliminar o modificar avisos de derechos de autor o marcas propietarias  
❌ Crear trabajos derivados basados en el software

---

## DESCARGO DE RESPONSABILIDAD

Este software se proporciona "tal cual", sin garantías de ningún tipo.
El autor no se hace responsable por daños o problemas derivados del uso del software.

---

## CONTACTO

Para consultas de licencia, uso comercial o permisos:

**Correo:** cgmagallanes23@gmail.com  
**Desarrollador:** Magallanes López Carlos Gabriel

---

**Última Actualización:** 16 de diciembre de 2025

---

## 👤 Autor

**Carlos Gabriel Magallanes López**

- **Institución:** CBTis No. 128
- **Correo:** cgmagallanes23@gmail.com
- **GitHub:** [@TheNarratorVIMXXX](https://github.com/TheNarratorVIMXXX)
- **Fecha:** Diciembre 2025

---

**© 2025 Carlos Gabriel Magallanes López. Todos los derechos reservados.**
