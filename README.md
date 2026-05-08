# 🎓 Sistema de Consultas Académicas con IA

> Web institucional para gestionar y automatizar procesos universitarios por medio de inteligencia artificial. Desplegado en **Vercel** usando base de datos **PostgreSQL en Neon**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 📋 Descripción

Sistema web académico que integra un **asistente virtual con inteligencia artificial** (Google Gemini) para ayudar a estudiantes universitarios con consultas.

---

## 🏗️ Arquitectura

`	ext
Navegador (Frontend) -> Vercel (Hosting)
    │
    ▼
Flask (app.py) ──► Templates HTML & Static Files
    │
    ├──► PostgreSQL (Neon DB) ──► Usuarios & Historial de Chat
    │
    └──► LangChain ──► API de Google Gemini 2.5 Flash
`

---

## 📁 Estructura del Proyecto

`	ext
Proyecto-Final-Desarrollo-De-Software-Web-Institucional/
│
├── 📂 static/                  # Archivos CSS y JS (Frontend)
├── 📂 templates/               # Plantillas HTML (Jinja2)
├── 📂 Documentacion/           # Documentación del proyecto
│
├── app.py                      # Backend principal (Flask + IA + BD)
├── gestionar_usuarios.py       # HERRAMIENTA CLI: CRUD de usuarios (Panel de Control)
├── init_neon_db.py             # Script de inicialización de BD
├── requirements.txt            # Dependencias de Python consolidadas
├── vercel.json                 # Configuración de despliegue Serverless en Vercel
├── docker-compose.yml          # Orquestación local (Flask + Postgres)
└── README.md                   # Este archivo
`

---

## 🚀 Instalación y Ejecución Local

### Requisitos Previos

- Python 3.8+
- API Key de [Google Gemini](https://aistudio.google.com/app/apikey)
- Base de datos PostgreSQL (local o en Neon)

### Configuracion Rápida

1. Clonar el repositorio y crear el entorno virtual:
\\\ash
git clone https://github.com/BrayanUrquijo/Proyecto-Final-Desarrollo-De-Software-Web-Institucional.git
cd Proyecto-Final-Desarrollo-De-Software-Web-Institucional
python -m venv .venv
.\.venv\Scripts\activate
\\\

2. Instalar dependencias:
\\\ash
pip install -r requirements.txt
\\\

3. Configurar variables de entorno (\.env\):
\\\env
GEMINI_API_KEY=tu_api_key_aqui
DATABASE_URL=postgresql://usuario:password@localhost:5432/bd
FLASK_SECRET_KEY=clave_secreta_aleatoria
\\\

4. Inicializar DB e iniciar servidor:
\\\ash
python app.py
\\\

---

## 🔑 Gestión de Usuarios (CRUD)

Las credenciales ya no están quemadas en código, ahora se administran dinámicamente en la base de datos (Neon/Local) con una herramienta interactiva.

Ejecuta el panel administrativo desde tu terminal:
\\\ash
python gestionar_usuarios.py
\\\

**Opciones del panel:**
1. Crear nuevo usuario
2. Modificar usuario (cambiar nombre o contraseña)
3. Eliminar usuario (limpiando su historial de chat automáticamente)
4. Listar usuarios registrados

---

## 🐳 Ejecución con Docker Local

Si prefieres usar contenedores, el proyecto incluye un entorno preconfigurado de Postgres:
\\\ash
docker-compose up -d
\\\

---

## ☁️ Despliegue en Vercel

El proyecto está preparado para funcionar como App Serverless.
1. Crea un proyecto en Vercel apuntando a este repositorio.
2. Agrega las variables de entorno en Settings > Environment Variables (\DATABASE_URL\ de Neon y \GEMINI_API_KEY\).
3. Vercel ruteará automáticamente las peticiones gracias al archivo \ercel.json\.

---

## 🗺️ Roadmap Actualizado

- [x] Sistema de login y autenticación.
- [x] Chat con asistente de IA (Gemini).
- [x] Interfaz web responsive.
- [x] Gestión segura de API keys y DB strings (\.env\).
- [x] Migración total de credenciales y BD a PostgreSQL.
- [x] Panel de Administrador CLI (\gestionar_usuarios.py\).
- [x] Despliegue en producción en la nube (Vercel Serverless + NeonDB).
- [x] Historial de conversaciones persistente.
- [ ] Seguridad extra de contraseñas hasheadas en BD.
- [ ] Integración con APIs de horarios institucionales.

---

## 👤 Autor

**Brayan Urquijo**
- GitHub: [@BrayanUrquijo](https://github.com/BrayanUrquijo)

---
<p align="center">
  Hecho con ❤️ y 🤖 IA para estudiantes universitarios
</p>