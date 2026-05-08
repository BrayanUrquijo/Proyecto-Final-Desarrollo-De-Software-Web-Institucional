# 🎓 Sistema de Consultas Académicas con IA

> Web institucional para gestionar y automatizar procesos universitarios por medio de inteligencia artificial.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜-green?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 📋 Descripción

Sistema web académico que integra un **asistente virtual con inteligencia artificial** (Google Gemini) para ayudar a estudiantes universitarios con consultas sobre:

- 📊 Consultas sobre calificaciones
- 📝 Proceso de admisión y matrícula
- 📄 Solicitud de certificados y documentos
- 📅 Horarios de clase
- 📞 Información de contacto
- 🔧 Resolución de dudas administrativas

---

## 🖼️ Vistas de la Aplicación

### Página de Login
- Interfaz de autenticación con diseño institucional
- Validación de credenciales contra el backend
- Mensajes de error y éxito visuales

### Dashboard con Chat IA
- Panel lateral de navegación
- Tarjetas de consultas rápidas predefinidas
- Chat en tiempo real con el asistente de IA
- Historial de conversación por usuario

---

## 🏗️ Arquitectura

```
Navegador (HTML/CSS/JS)
    │
    ▼
Flask (app.py) ──► Templates HTML (Jinja2)
    │
    ├──► API REST (autenticación)
    │
    └──► LangChain ──► Google Gemini 2.5 Flash
```

---

## 📁 Estructura del Proyecto

```
Proyecto-Final-Desarrollo-De-Software-Web-Institucional/
│
├── 📂 static/                  # Archivos estáticos
│   ├── 📂 css/
│   │   ├── login.css           # Estilos del login
│   │   └── styles.css          # Estilos del dashboard
│   └── 📂 js/
│       ├── login.js            # Lógica de autenticación
│       └── dashboard.js        # Lógica del chat con IA
│
├── 📂 templates/               # Plantillas HTML (Jinja2)
│   ├── login.html              # Página de inicio de sesión
│   └── dashboard.html          # Panel principal con chat
│
├── 📂 Documentacion/           # Documentación del proyecto
│   ├── INICIO_RAPIDO.md
│   ├── INSTALACION_GEMINI.md
│   ├── GUIA_COMPLETA_WEB.md
│   └── COMPARATIVA.md
│
├── app.py                      # Backend principal (Flask + Gemini)
├── requirements_web.txt        # Dependencias del proyecto web
├── requirements_gemini.txt     # Dependencias de Gemini standalone
├── Dockerfile                  # Configuración de Docker
├── docker-compose.yml          # Orquestación de contenedores
└── README.md                   # Este archivo
```

---

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Una API Key de [Google Gemini](https://aistudio.google.com/app/apikey)

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/BrayanUrquijo/Proyecto-Final-Desarrollo-De-Software-Web-Institucional.git
cd Proyecto-Final-Desarrollo-De-Software-Web-Institucional
```

### Paso 2: Crear entorno virtual

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements_web.txt
pip install python-dotenv
```

### Paso 4: Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
# API Keys
GEMINI_API_KEY=tu_api_key_de_google_gemini

# Flask
FLASK_SECRET_KEY=tu_clave_secreta_aqui
```

> ⚠️ **Nunca subas el archivo `.env` a GitHub.** Ya está incluido en el `.gitignore`.

### Paso 5: Ejecutar el servidor

```bash
python app.py
```

Accede a: **http://localhost:5000**

---

## 🔑 Credenciales de Prueba

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `2459407-3743` | `admin123` | Administrador |
| `estudiante` | `pass123` | Estudiante |
| `demo` | `demo` | Demo |

> En futuras versiones, las credenciales se almacenarán en PostgreSQL con contraseñas hasheadas (bcrypt).

---

## 🔌 Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/login` | Iniciar sesión |
| `POST` | `/api/logout` | Cerrar sesión |
| `GET` | `/api/check-session` | Verificar sesión activa |

### Chat con IA

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/chat` | Enviar mensaje al asistente |
| `POST` | `/api/clear-chat` | Limpiar historial de conversación |

### Utilidades

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/health` | Verificar estado del servidor |

---

## 🐳 Ejecución con Docker

```bash
docker-compose up -d
```

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| Backend (Flask) | `5000` | Servidor principal |
| Frontend (Nginx) | `8080` | Servidor estático |

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| **Python** | 3.8+ | Lenguaje principal del backend |
| **Flask** | 3.0 | Framework web |
| **Google Gemini** | 2.5 Flash | Modelo de IA para el asistente |
| **LangChain** | 0.1+ | Orquestación del modelo de IA |
| **HTML5/CSS3/JS** | - | Frontend |
| **Docker** | - | Contenedorización |
| **python-dotenv** | - | Gestión de variables de entorno |

---

## 🗺️ Roadmap

- [x] Sistema de login y autenticación
- [x] Chat con asistente de IA (Gemini)
- [x] Interfaz web responsive
- [x] Gestión segura de API keys (`.env`)
- [x] Dockerización del proyecto
- [ ] Migración de usuarios a PostgreSQL
- [ ] Contraseñas hasheadas con bcrypt
- [ ] API de fecha y hora del servidor
- [ ] Integración con APIs de horarios
- [ ] Registro de nuevos usuarios
- [ ] Historial de conversaciones persistente

---

## 📚 Documentación

Consulta la carpeta [`Documentacion/`](./Documentacion/) para guías detalladas:

| Documento | Contenido |
|-----------|-----------|
| [INICIO_RAPIDO.md](./Documentacion/INICIO_RAPIDO.md) | Guía rápida de instalación |
| [INSTALACION_GEMINI.md](./Documentacion/INSTALACION_GEMINI.md) | Configuración de Google Gemini |
| [GUIA_COMPLETA_WEB.md](./Documentacion/GUIA_COMPLETA_WEB.md) | Documentación técnica completa |
| [COMPARATIVA.md](./Documentacion/COMPARATIVA.md) | Comparativa de tecnologías |


## 👤 Autor

**Brayan Urquijo**

- GitHub: [@BrayanUrquijo](https://github.com/BrayanUrquijo)

---

## 📄 Licencia

Este proyecto es parte de un **Proyecto Final de Desarrollo de Software Web Institucional** con fines académicos.

---

<p align="center">
  Hecho con ❤️ y 🤖 IA para estudiantes universitarios
</p>
