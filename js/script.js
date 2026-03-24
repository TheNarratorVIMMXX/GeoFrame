/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/*                                                                  Scripts para el Proyecto GeoFrame                                                                        */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/* Autor: Magallanes López Carlos Gabriel                                                                                                                                    */
/* Versión del Proyecto: 1.0                                                                                                                                                 */
/* Correo: cgmagallanes23@gmail.com                                                                                                                                          */
/* Ultima Modificación: 23/03/2025                                                                                                                                           */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/

// Efecto Cursor Personalizado
const cursor = document.getElementById('cursor');                                                  // Obtener Elemento del Cursor Personalizado                 
const ring = document.getElementById('cursorRing');                                                // Obtener Elemento del Anillo del Cursor Personalizado
let mx = 0, my = 0, rx = 0, ry = 0;                                                                // Variables de Posición Mouse (mx, my) y Posición Anillo (rx, ry)
document.addEventListener('mousemove',coords => {mx = coords.clientX; my = coords.clientY});       // Actualizar Posición del Mouse en Variables mx y my al Mover el Mouse
(function loop(){                                                                                  // Función de Bucle para Animar el Anillo del Cursor
    rx += (mx - rx) * 0.12;                                                                        // Suavizar Movimiento Horizontal del Anillo al Mouse con Factor Suavizado
    ry += (my - ry) * 0.12;                                                                        // Suavizar Movimiento Vertical del Anillo al Mouse con Factor Suavizado
    cursor.style.left = mx - 3 + 'px';                                                             // Posicionar Cursor en la Posición Izquierda del Mouse 
    cursor.style.top = my - 3 + 'px';                                                              // Posicionar Cursor en la Posición Superior del Mouse
    ring.style.left = rx - 14 + 'px';                                                              // Posicionar Anillo en la Posición Izquierda del Mouse con Suavizado
    ring.style.top = ry - 14 + 'px';                                                               // Posicionar Anillo en la Posición Superior del Mouse con Suavizado
    requestAnimationFrame(loop);                                                                   // Solicitar el Siguiente Frame para Continuar el Bucle de Animación
})();
const linksNButtons = document.querySelectorAll('a,button');                                       // Seleccionar Todos los Elementos 'a' y 'button' para Agregar Efecto Hover
linksNButtons.forEach(element=>{                                                                   // Aplicar Función a cada Elemento Seleccionado
  element.addEventListener(                                                                        // Agregar Evento Mouse Enter para Aumentar Tamaño Anillo y Reducir Opacidad
    'mouseenter', 
    () => {ring.style.width='50px'; ring.style.height='50px'; ring.style.opacity='.3'}
  );                                                                                             
  element.addEventListener(                                                                        // Agregar Evento Mouse Leave para Restaurar Tamaño y Opacidad Original
    'mouseleave',
    () => {ring.style.width='28px'; ring.style.height='28px'; ring.style.opacity='.5'}
  );
});

// Efecto Fade In al hacer Scroll
const observer = new IntersectionObserver((entries) => {                                           // Instanciar Observador Intersección, Detección Elementos en Viewport 
    entries.forEach(entry => {                                                                     // Para Cada Elemento Detectado en el Viewport
        if (entry.isIntersecting){                                                                 // Si esta en Viewport
            entry.target.classList.add('visible');                                                 // Agregar Clase 'visible' para Efecto Fade In
            observer.unobserve(entry.target);                                                      // Dejar de Observar el Elemento para Mejorar Rendimiento
        }                         
    });
}, {threshold: 0.1});                                                                              // Configuración del Observador: Activar cuando el 10% del Elemento sea Visible

// Observar Elementos de la Clase 'Fade-In' para Activar Efecto al Entrar en el Viewport
const revealElements = document.querySelectorAll('.reveal');                                       // Seleccionar Todos los Elementos con Clase 'reveal' 
revealElements.forEach(element => observer.observe(element));                                      // Observar Cada Elemento para Activar Efecto Fade In al Entrar en el Viewport                         

/*****************************************************************************************************************************************************************************/