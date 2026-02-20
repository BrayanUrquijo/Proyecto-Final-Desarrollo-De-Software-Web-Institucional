# 🌐 Guía Completa de la Aplicación Web

## Arquitectura

La aplicación utiliza una arquitectura **monolítica con Flask** que sirve tanto el frontend (HTML/CSS/JS) como el backend (API REST + IA).

```
Navegador → Flask (app.py) → Templates HTML
                            → API REST → Google Gemini
```

## Componentes

### Backend (app.py)

El archivo principal maneja:

- **Rutas de páginas:** Sirve `login.html` y `dashboard.html`
- **API de autenticación:** Login/logout con sesiones de Flask
- **API de chat:** Comunicación con Google Gemini via LangChain
- **Gestión de historial:** Mantiene conversaciones por usuario

### Frontend

| Archivo | Ubicación | Función |
|---------|-----------|---------|
| `login.html` | `templates/` | Página de inicio de sesión |
| `dashboard.html` | `templates/` | Panel principal con chat IA |
| `login.css` | `static/css/` | Estilos de la página de login |
| `styles.css` | `static/css/` | Estilos del dashboard |
| `login.js` | `static/js/` | Lógica de autenticación |
| `dashboard.js` | `static/js/` | Lógica del chat con IA |

## Endpoints de la API

### Autenticación

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/api/login` | Iniciar sesión |
| `POST` | `/api/logout` | Cerrar sesión |
| `GET` | `/api/check-session` | Verificar sesión activa |

#### Ejemplo - Login:
```json
POST /api/login
{
    "username": "demo",
    "password": "demo"
}

// Respuesta exitosa:
{
    "success": true,
    "message": "Login exitoso",
    "username": "demo"
}
```

### Chat con IA

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/api/chat` | Enviar mensaje al asistente |
| `POST` | `/api/clear-chat` | Limpiar historial de conversación |
| `GET` | `/health` | Verificar estado del servidor |

#### Ejemplo - Chat:
```json
POST /api/chat
{
    "message": "¿Cómo consulto mis calificaciones?"
}

// Respuesta:
{
    "response": "Para consultar tus calificaciones...",
    "session_id": "demo"
}
```

## Flujo de la Aplicación

1. El usuario accede a `http://localhost:5000`
2. Es redirigido a `/login`
3. Ingresa credenciales → `POST /api/login`
4. Si es exitoso, redirige a `/dashboard`
5. En el dashboard, escribe preguntas → `POST /api/chat`
6. El backend envía la pregunta a Gemini y devuelve la respuesta
7. El historial se mantiene durante la sesión

## Personalización del Asistente

El comportamiento del asistente se define en el `SYSTEM_PROMPT` de `app.py`:

```python
SYSTEM_PROMPT = """
Eres un asistente virtual para un sistema académico universitario.
Ayudas a estudiantes con:
- Consultas sobre calificaciones
- Proceso de admisión y matrícula
- Solicitud de certificados y documentos
...
"""
```

Modifica este prompt para cambiar la personalidad y conocimientos del asistente.

## Despliegue con Docker

```bash
docker-compose up -d
```

Esto levanta:
- **Backend Flask** en el puerto `5000`
- **Frontend Nginx** en el puerto `8080` (para la versión estática)