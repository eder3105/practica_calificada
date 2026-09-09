PRÁCTICA CALIFICADA 1: CONTENEDORES Y MICROSERVICIOS

Alumno: Ederd Carrasco Oscco
Repositorio GitHub: https://github.com/eder3105/practica_calificada.git

---

DESCRIPCIÓN DE LOS CASOS

El proyecto consta de dos microservicios contenedorizados con Docker:
1. Caso 1 (Descargador Web): Aplicación interactiva con Flask y yt-dlp (con soporte multimedia para ffmpeg) para descargar videos de redes sociales.
2. Caso 2 (Automatización Web): Script en Python con Selenium y Chromium en modo headless para consultar datos electorales y exportar los resultados a Excel.

---

REQUISITOS PREVIOS
- Tener Docker Desktop instalado y abierto en tu computadora.
- Tener Git instalado.

---

GUÍA DE INSTALACIÓN Y PRUEBA

CASO 1: Descargador de Redes Sociales
1. Abre tu terminal y entra a la carpeta del caso:
   cd caso1
2. Construye la imagen Docker:
   docker build -t caso1-app:v1.0 .
3. Ejecuta el contenedor:
   docker run -d -p 5000:5000 --name caso1-container caso1-app:v1.0
4. Cómo probarlo: Abre tu navegador web y entra a http://localhost:5000

CASO 2: Automatización con Selenium
1. Entra a la carpeta del caso:
   cd caso2
2. Construye la imagen Docker:
   docker build -t caso2-app:v1.0 .
3. Ejecuta el contenedor de prueba:
   docker run --rm caso2-app:v1.0
4. Cómo probarlo: La terminal arrojará automáticamente el mensaje de éxito de la automatización y generará el Excel de resultados.

---