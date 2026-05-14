/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/*                                                                  Scripts para el Proyecto GeoFrame                                                                        */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/* Autor: Magallanes López Carlos Gabriel                                                                                                                                    */
/* Versión del Proyecto: 1.0                                                                                                                                                 */
/* Correo: cgmagallanes23@gmail.com                                                                                                                                          */
/* Ultima Modificación: 23/03/2026                                                                                                                                           */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/

// i18n - Traducciones
const translations = {
    es: {
        // Header
        headerCenter:       "OPTIMIZADOR DE VENTANA NORMANDA",
        headerFund:         "FUNDAMENTO",
        headerMod:          "MÓDULOS",
        headerPreview:      "PREVIEW",
        headerDl:           "↓ DESCARGAR",
        // Hero
        heroEyebrow:        "Optimización con restricciones · Cálculo diferencial",
        heroDesc:           "Calcula y visualiza las dimensiones exactas de una ventana normanda que maximizan el área disponible dado un perímetro fijo.",
        heroDl:             "↓ GeoFrame.exe",
        heroGh:             "GitHub →",
        // SVG labels
        svgAncho:           "ANCHO",
        svgAlt:             "ALT",
        svgRect:            "RECTÁNGULO",
        svgSemi:            "SEMICÍRCULO",
        // Metrics
        metric1Val:         "4",
        metric1Label:       "Paneles de\nvisualización",
        metric2Label:       "Rango de\nperímetro",
        metric3Label:       "Precisión\nnumérica",
        metric4Label:       "Dependencias\nde instalación",
        // Math Section
        mathNum:            "01 — FUNDAMENTO MATEMÁTICO",
        mathHeading:        "El problema de <em>optimización</em>",
        mathBody:           "Dado un perímetro fijo P, se busca la distribución óptima entre ancho y alto que produce el área máxima posible.",
        eqTag1:             "RESTRICCIÓN",
        eqTag2:             "DESPEJANDO y",
        eqTag3:             "ÁREA TOTAL",
        eqTag4:             "dA/dx = 0",
        eqTag5:             "ÓPTIMO",
        eqTag6:             "VERIFICACIÓN",
        // Modules Section
        modNum:             "02 — MÓDULOS DEL SISTEMA",
        modHeading:         "<em>Cuatro</em> paneles de análisis",
        feat1Title:         "Ventana Normanda",
        feat1Body:          "Representación geométrica interactiva con anotaciones de dimensiones. Modos Normal, Detallado y Técnico.",
        feat2Title:         "Gráfica A(x)",
        feat2Body:          "Curva de la función de área frente al ancho. Punto máximo identificado visualmente con líneas de referencia dinámicas.",
        feat3Title:         "Resultados en Tiempo Real",
        feat3Body:          "Dimensiones óptimas x, y y radio del semicírculo actualizadas al instante con precisión de cuatro decimales.",
        feat4Title:         "Análisis de Sensibilidad",
        feat4Body:          "Variación del área máxima para cualquier perímetro en el rango 1–100 m con el punto actual resaltado.",
        // Figure Section
        figLabel:           "CAPTURA DE PANTALLA",
        figTitle:           "Interfaz completa de GeoFrame",
        // Download Section
        dlNum:              "03 — DESCARGA",
        dlBig:              "Sin instalación. <em>Ejecuta y listo.</em>",
        dlMain:             "↓ Descargar GeoFrame.exe",
        dlNote:             "WINDOWS · NO REQUIERE PYTHON · DOBLE CLIC",
        // Spec Table
        spec1Key:           "PLATAFORMA",
        spec1Val:           "Windows 10 / 11",
        spec2Key:           "DISTRIBUCIÓN",
        spec2Val:           "Ejecutable standalone",
        spec3Key:           "LENGUAJE",
        spec3Val:           "Python 3.11",
        spec4Key:           "LIBRERÍAS",
        spec4Val:           "Matplotlib, NumPy, SciPy, PyQt5",
        spec5Key:           "RESOLUCIÓN REC.",
        spec5Val:           "1920 × 1080 · Escala 100–150 %",
        spec6Key:           "AUTOR",
        spec6Val:           "Carlos Gabriel Magallanes López",
        spec7Key:           "FECHA DESARROLLO",
        spec7Val:           "Diciembre 2025",
        spec8Key:           "LICENCIA",
        spec8Val:           "Propietario · Uso personal y educativo",
        // Footer
        footerMeta1:        "© 2025 · Todos los derechos reservados",
        footerMeta2:        "cgmagallanes23@gmail.com · @TheNarratorVIMMXX",
        // Lang Button
        langBtn:            "🌐 English"
    },
    en: {
        // Header
        headerCenter:       "NORMAN WINDOW OPTIMIZER",
        headerFund:         "FOUNDATION",
        headerMod:          "MODULES",
        headerPreview:      "PREVIEW",
        headerDl:           "↓ DOWNLOAD",
        // Hero
        heroEyebrow:        "Constrained optimization · Differential calculus",
        heroDesc:           "Calculate and visualize the exact dimensions of a Norman window that maximize the available area given a fixed perimeter.",
        heroDl:             "↓ GeoFrame.exe",
        heroGh:             "GitHub →",
        // SVG labels
        svgAncho:           "WIDTH",
        svgAlt:             "HEIGHT",
        svgRect:            "RECTANGLE",
        svgSemi:            "SEMICIRCLE",
        // Metrics
        metric1Val:         "4",
        metric1Label:       "Visualization\npanels",
        metric2Label:       "Perimeter\nrange",
        metric3Label:       "Numerical\nprecision",
        metric4Label:       "Installation\ndependencies",
        // Math Section
        mathNum:            "01 — MATHEMATICAL FOUNDATION",
        mathHeading:        "The <em>optimization</em> problem",
        mathBody:           "Given a fixed perimeter P, we seek the optimal distribution between width and height that produces the maximum possible area.",
        eqTag1:             "CONSTRAINT",
        eqTag2:             "SOLVING FOR y",
        eqTag3:             "TOTAL AREA",
        eqTag4:             "dA/dx = 0",
        eqTag5:             "OPTIMUM",
        eqTag6:             "VERIFICATION",
        // Modules Section
        modNum:             "02 — SYSTEM MODULES",
        modHeading:         "<em>Four</em> analysis panels",
        feat1Title:         "Norman Window",
        feat1Body:          "Interactive geometric representation with dimension annotations. Normal, Detailed and Technical modes.",
        feat2Title:         "A(x) Graph",
        feat2Body:          "Area function curve versus width. Maximum point visually identified with dynamic reference lines.",
        feat3Title:         "Real-Time Results",
        feat3Body:          "Optimal dimensions x, y and semicircle radius updated instantly with four decimal precision.",
        feat4Title:         "Sensitivity Analysis",
        feat4Body:          "Maximum area variation for any perimeter in the 1–100 m range with the current point highlighted.",
        // Figure Section
        figLabel:           "SCREENSHOT",
        figTitle:           "Complete GeoFrame interface",
        // Download Section
        dlNum:              "03 — DOWNLOAD",
        dlBig:              "No install. <em>Run and go.</em>",
        dlMain:             "↓ Download GeoFrame.exe",
        dlNote:             "WINDOWS · NO PYTHON REQUIRED · DOUBLE CLICK",
        // Spec Table
        spec1Key:           "PLATFORM",
        spec1Val:           "Windows 10 / 11",
        spec2Key:           "DISTRIBUTION",
        spec2Val:           "Standalone executable",
        spec3Key:           "LANGUAGE",
        spec3Val:           "Python 3.11",
        spec4Key:           "LIBRARIES",
        spec4Val:           "Matplotlib, NumPy, SciPy, PyQt5",
        spec5Key:           "REC. RESOLUTION",
        spec5Val:           "1920 × 1080 · Scale 100–150%",
        spec6Key:           "AUTHOR",
        spec6Val:           "Carlos Gabriel Magallanes López",
        spec7Key:           "DEV DATE",
        spec7Val:           "December 2025",
        spec8Key:           "LICENSE",
        spec8Val:           "Proprietary · Personal and educational use",
        // Footer
        footerMeta1:        "© 2025 · All rights reserved",
        footerMeta2:        "cgmagallanes23@gmail.com · @TheNarratorVIMMXX",
        // Lang Button
        langBtn:            "🌐 Español"
    }
};

// Detección y Aplicación de Idioma
function detectLanguage() {
    const saved = localStorage.getItem('lang');                                                  // Obtener el Lenguaje del Local Storage
    if (saved) return saved;                                                                     // Si se obtuvo el Lenguaje del Local Storage Retornar
    const browserLang = navigator.language || navigator.userLanguage;                            // Obtener el Lenguaje del Browser
    return browserLang.startsWith('es') ? 'es' : 'en';                                          // Español si es es-*, inglés para todo lo demás
}

// Aplicar Traducciones al DOM
function applyLanguage(lang) {
    const t = translations[lang];
    document.querySelectorAll('[data-i18n]').forEach(el => {                                     // Traducir Elementos con Texto Simple
        const key = el.getAttribute('data-i18n');
        if (t[key]) el.innerHTML = t[key];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(el => {                                // Traducir Elementos con HTML Interno
        const key = el.getAttribute('data-i18n-html');
        if (t[key]) el.innerHTML = t[key];
    });
    document.documentElement.setAttribute('lang', lang);                                         // Actualizar Atributo lang del HTML para Accesibilidad
    const btn = document.getElementById('langToggleBtn');
    if (btn) btn.textContent = t.langBtn;
    localStorage.setItem('lang', lang);                                                          // Guardar Idioma Seleccionado en localStorage
}

// Crear Botón Flotante de Cambio de Idioma
function createLangButton() {
    const btn = document.createElement('button');                                                // Crear el Elemento
    btn.id = 'langToggleBtn';                                                                    // ID para Aplicar Estilos desde CSS
    btn.addEventListener('click', () => {                                                        // Agregar Callback para el Botón
        const current = localStorage.getItem('lang') || detectLanguage();                        // Obtener Lenguaje Actual
        const next = current === 'es' ? 'en' : 'es';                                            // Alternar entre Español e Inglés
        applyLanguage(next);                                                                     // Aplicar el Lenguaje
    });
    document.body.appendChild(btn);                                                              // Agregar Botón al Documento
}

// Efecto Cursor Personalizado
const cursor = document.getElementById('cursor');                                                // Obtener Elemento del Cursor Personalizado
const ring = document.getElementById('cursorRing');                                              // Obtener Elemento del Anillo del Cursor Personalizado
let mx = 0, my = 0, rx = 0, ry = 0;                                                              // Variables de Posición Mouse (mx, my) y Posición Anillo (rx, ry)
document.addEventListener('mousemove', coords => {mx = coords.clientX; my = coords.clientY});   // Actualizar Posición del Mouse
(function loop() {                                                                               // Función de Bucle para Animar el Anillo del Cursor
    rx += (mx - rx) * 0.12;                                                                      // Suavizar Movimiento Horizontal
    ry += (my - ry) * 0.12;                                                                      // Suavizar Movimiento Vertical
    cursor.style.left = mx - 3 + 'px';
    cursor.style.top  = my - 3 + 'px';
    ring.style.left   = rx - 14 + 'px';
    ring.style.top    = ry - 14 + 'px';
    requestAnimationFrame(loop);                                                                 // Solicitar el Siguiente Frame
})();
const linksNButtons = document.querySelectorAll('a, button');                                    // Seleccionar Todos los Elementos 'a' y 'button'
linksNButtons.forEach(element => {
    element.addEventListener('mouseenter', () => {ring.style.width='50px'; ring.style.height='50px'; ring.style.opacity='.3'});
    element.addEventListener('mouseleave', () => {ring.style.width='28px'; ring.style.height='28px'; ring.style.opacity='.5'});
});

// Efecto Fade In al hacer Scroll
const observer = new IntersectionObserver((entries) => {                                         // Instanciar Observador Intersección
    entries.forEach(entry => {                                                                   // Para Cada Elemento Detectado en el Viewport
        if (entry.isIntersecting) {                                                              // Si esta en Viewport
            entry.target.classList.add('visible');                                               // Agregar Clase 'visible' para Efecto Fade In
            observer.unobserve(entry.target);                                                    // Dejar de Observar el Elemento
        }
    });
}, { threshold: 0.1 });                                                                          // Activar cuando el 10% del Elemento sea Visible

const revealElements = document.querySelectorAll('.reveal');                                     // Seleccionar Todos los Elementos con Clase 'reveal'
revealElements.forEach(element => observer.observe(element));                                    // Observar Cada Elemento

// Inicialización
createLangButton();                                                                              // Creación del Botón del Lenguaje
applyLanguage(detectLanguage());                                                                 // Aplicación del Lenguaje

/*****************************************************************************************************************************************************************************/
