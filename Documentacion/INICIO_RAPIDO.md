# 🚀 Inicio Rápido

## Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Una API Key de Google Gemini

## Instalación en 5 pasos

### 1. Clonar el proyecto
```bash
git clone <url-del-repositorio>
cd PROYECTO-FINAL-DESARROLLO
```

### 2. Crear entorno virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements_web.txt
```

### 4. Configurar API Key de Gemini
Pegar tu api key en `.env` en la raíz del proyecto:
```
TU_API_KEY_AQUI
```

> Para obtener una API Key, visita: https://aistudio.google.com/app/apikey

### 5. Ejecutar el servidor
```bash
python app.py
```

Accede a: **http://localhost:5000**

## Credenciales de Prueba

| Usuario | Contraseña |
|---------|------------|
| `2459407-3743` | `admin123` |
| `estudiante` | `pass123` |
| `demo` | `demo` |

## Estructura del Proyecto
```
PROYECTO-FINAL-DESARROLLO/
├── static/
│   ├── css/
│   │   ├── login.css
│   │   └── styles.css
│   └── js/
│       ├── login.js
│       └── dashboard.js
├── templates/
│   ├── login.html
│   └── dashboard.html
├── Documentacion/
│   ├── INICIO_RAPIDO.md
│   ├── INSTALACION_GEMINI.md
│   ├── GUIA_COMPLETA_WEB.md
│   └── COMPARATIVA.md
├── app.py
├── config_gemini.txt
├── requirements_web.txt
├── requirements_gemini.txt
├── docker-compose.yml
└── Dockerfile
```