Markdown

# 🎫 EventFinder con Reflex & Ticketmaster

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Reflex](https://img.shields.io/badge/Reflex-Framework-black)
![API](https://img.shields.io/badge/API-Ticketmaster-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> Una aplicación web full-stack moderna para buscar y explorar eventos, conciertos y deportes en tiempo real, construida puramente en Python utilizando el framework Reflex.

## 📖 Descripción

Este proyecto es una demostración de la potencia de **[Reflex](https://reflex.dev/)** para crear aplicaciones web interactivas (Frontend y Backend) utilizando únicamente Python. La aplicación se conecta a la **API Discovery de Ticketmaster** para permitir a los usuarios buscar eventos por palabras clave, ciudad, clasificación (música, deportes, arte) y fechas.

## ✨ Características Principales

* 🔎 **Búsqueda en Tiempo Real:** Consulta eventos directamente desde la base de datos de Ticketmaster.
* 🎨 **Interfaz Reactiva:** UI moderna y responsiva construida con componentes de Reflex.
* 📍 **Filtros Dinámicos:** Filtrado por ciudad, género musical o tipo de evento.
* 📅 **Detalles del Evento:** Visualización de fechas, horarios, precios y enlaces directos de compra.
* 🌓 **Modo Oscuro/Claro:** Soporte nativo de temas visuales.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework Web:** [Reflex](https://reflex.dev/)
* **Peticiones HTTP:** `requests`
* **API Externa:** [Ticketmaster Discovery API](https://developer.ticketmaster.com/)

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Prerrequisitos

* Tener instalado **Python 3.8** o superior.
* Obtener una **API Key** gratuita en el [Portal de Desarrolladores de Ticketmaster](https://developer.ticketmaster.com/).

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Nakajito/ticketmaster_app
cd ticketmaster_app
```
### 3. Crear Entorno Virtual (Recomendado)
``` bash
python -m venv .venv

# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
source .venv/bin/activate
```
### 4. Instalar Dependencias
``` bash
pip install -r requirements.txt
```
Si no tienes un archivo requirements.txt, asegúrate de instalar al menos:

``` bash
pip install reflex requests
```
### 5. Configurar Variables de Entorno
Por seguridad, no subas tu API Key al código. Crea un archivo .env en la raíz del proyecto:

``` bash
touch .env  # O crea el archivo manualmente en Windows
```
Abre el archivo .env y agrega tu clave:

``` bash
TICKETMASTER_API_KEY=tu_clave_secreta_aqui
```
### 6. Inicializar y Correr la App
Inicializa el proyecto (si es la primera vez que lo descargas):

``` bash
reflex init
```
Ejecuta el servidor de desarrollo:

``` bash
reflex run
```
La aplicación estará disponible en: http://localhost:3000

📂 Estructura del Proyecto
``` Plaintext

├── assets/              # Imágenes y recursos estáticos
├── rxconfig.py          # Configuración principal de Reflex
├── .env                 # Variables de entorno (NO SUBIR A GITHUB)
├── requirements.txt     # Dependencias del proyecto
└── nombre_proyecto/     # Código fuente
    ├── __init__.py
    ├── nombre_proyecto.py  # Archivo principal de la App
    ├── state.py         # Lógica de estado y llamadas a la API
    └── components/      # Componentes UI reutilizables (Navbar, Cards, etc.)
```
### 🤝 Contribución
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la búsqueda o el diseño:

Haz un Fork del proyecto.

Crea una rama para tu funcionalidad (git checkout -b feature/NuevaFuncionalidad).

Haz Commit de tus cambios (git commit -m 'Agrega nueva funcionalidad').

Haz Push a la rama (git push origin feature/NuevaFuncionalidad).

Abre un Pull Request.

### 📄 Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo LICENSE para más detalles.

### 👤 Autor
Daniel - Desarrollador Full Stack

***

### Consejos adicionales para tu proyecto:

1.  **Archivo `.gitignore`:** Asegúrate de tener un archivo `.gitignore` bien configurado para **no subir** tu archivo `.env` ni la carpeta `__pycache__`. Reflex suele crear uno por defecto, pero revisa que incluya:
    ```gitignore
    .env
    .venv/
    __pycache__/
    .web/
    ```
2.  **Requirements:** Si aún no generas tu archivo de dependencias, ejecuta `pip freeze > requirements.txt` en tu terminal antes de subir el código.

3.  **State de Reflex:** En la sección "Estructura del Proyecto" del README, he separado `state.py` y `components/`. Si tu proyecto tiene todo en un solo archivo, puedes ajustar esa parte, pero separar el estado (lógica) de la UI es una buena práctica en Reflex.