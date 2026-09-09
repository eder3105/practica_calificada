Práctica Calificada 1 - Contenedores y Microservicios

Alumno: Ederd Luis

URL del Repositorio:
https://github.com/eder3105/practica_calificada.git

---

DESCRIPCIÓN GENERAL
Este proyecto implementa dos casos de estudio utilizando contenedores Docker para garantizar el aislamiento, la portabilidad y la correcta ejecución de dependencias complejas del sistema operativo (como ffmpeg y Chromium):
- Caso 1: Aplicación web en Flask combinada con yt-dlp para la descarga de contenido multimedia desde plataformas de redes sociales.
- Caso 2: Script de automatización web utilizando Python, Selenium y un entorno con Chromium ejecutándose de manera headless en un contenedor optimizado.

---

PASOS DE INSTALACIÓN Y EJECUCIÓN

Prerrequisitos:
- Tener instalado Docker y Docker Desktop activos en el equipo.
- Tener instalado Git para clonar y gestionar el repositorio.

Caso 1: Descargador de Redes Sociales (Flask + yt-dlp)
1. Navegar a la carpeta del caso:
   cd caso1
2. Construir la imagen de Docker:
   docker build -t caso1-app:v1.0 .
3. Ejecutar el contenedor mapeando el puerto 5000:
   docker run -d -p 5000:5000 --name caso1-container caso1-app:v1.0
4. Verificación:
   Abre tu navegador web e ingresa a http://localhost:5000

Caso 2: Automatización con Selenium y Chromium
1. Navegar a la carpeta del caso:
   cd ../caso2
2. Construir la imagen de Docker:
   docker build -t caso2-app:v1.0 .
3. Ejecutar el contenedor para verificar los logs de automatización:
   docker run --rm caso2-app:v1.0
4. Verificación:
   La terminal mostrará el mensaje de confirmación de la ejecución exitosa del script de Selenium dentro del entorno aislado.

---

CONCLUSIONES
- La utilización de Docker facilita enormemente la gestión de dependencias complejas (como controladores de navegación y herramientas multimedia), evitando conflictos con el sistema operativo local.
- La estructuración del proyecto en microservicios independientes permite aislar fallos, mejorar la escalabilidad y facilitar el control de versiones en repositorios remotos.