# GUIA COMPLETA: Sistema Web con IA desde CERO

## ¿Que acabas de recibir?

Un sistema web completo que incluye:
- **Frontend**: Interfaz web (HTML + CSS + JavaScript)
- **Backend**: Servidor Python (Flask) conectado a Gemini
- **Docker**: Para ejecutar todo facilmente

## PARTE 1: Entender la estructura

```
proyecto-web-ia/
├── index.html              # Pagina principal (lo que ves en el navegador)
├── styles.css              # Estilos visuales
├── script.js               # Logica del frontend (enviar mensajes)
├── app.py                  # Backend (servidor Flask + Gemini)
├── config_gemini.txt       # Tu API key de Gemini
├── requirements_web.txt    # Librerias de Python necesarias
├── Dockerfile              # Instrucciones para crear contenedor
└── docker-compose.yml      # Orquestacion de servicios
```

## PARTE 2: Como funciona todo (Explicacion simple)

### Frontend (HTML/CSS/JS)
```
Usuario escribe pregunta
    ↓
JavaScript captura el texto
    ↓
Envia peticion HTTP al backend
    ↓
Espera respuesta
    ↓
Muestra respuesta en pantalla
```

### Backend (Python Flask)
```
Recibe peticion del frontend
    ↓
Lee la pregunta
    ↓
Envia pregunta a Gemini
    ↓
Gemini responde
    ↓
Devuelve respuesta al frontend
```

## PARTE 3: Opcion 1 - SIN Docker (Mas facil para empezar)

### Paso 1: Preparar el entorno
```powershell
# Crear carpeta del proyecto
mkdir proyecto-web-ia
cd proyecto-web-ia

# Copiar todos los archivos que te di aqui
```

### Paso 2: Instalar dependencias
```powershell
# Crear entorno virtual
python -m venv .venv

# Activar
.venv\Scripts\Activate.ps1

# Instalar
pip install -r requirements_web.txt
```

### Paso 3: Iniciar el backend
```powershell
# En una terminal
python app.py
```

Deberia decir: "Backend corriendo en: http://localhost:5000"

### Paso 4: Abrir el frontend
```powershell
# Simplemente abre index.html en tu navegador
# Doble click en el archivo
```

O si quieres un servidor local:
```powershell
# En OTRA terminal
python -m http.server 8080
```

Luego abre: http://localhost:8080

### ¡LISTO! Ya funciona
- Frontend: http://localhost:8080
- Backend: http://localhost:5000

## PARTE 4: Opcion 2 - CON Docker (Profesional)

### ¿Que es Docker?

Docker es como una "caja magica" que empaqueta tu aplicacion con todo lo que necesita.

**Sin Docker:**
- "En mi computadora funciona"
- Problemas de dependencias
- Configuracion manual

**Con Docker:**
- Funciona igual en cualquier computadora
- Todo incluido
- Un solo comando para correr todo

### Instalar Docker

1. Descarga Docker Desktop: https://www.docker.com/products/docker-desktop/
2. Instala y reinicia tu PC
3. Abre Docker Desktop (debe estar corriendo)

### Usar Docker

```powershell
# En la carpeta del proyecto

# Construir y ejecutar TODO con un comando
docker-compose up --build
```

Eso es todo! Docker:
1. Descarga Python
2. Instala dependencias
3. Inicia el backend
4. Inicia el frontend
5. Todo funciona automaticamente

**Acceder:**
- Frontend: http://localhost:8080
- Backend: http://localhost:5000

**Detener:**
```powershell
Ctrl + C

# O en otra terminal:
docker-compose down
```

## PARTE 5: ¿Como modificar el proyecto?

### Cambiar el diseño (colores, textos)
Edita: `styles.css`

Ejemplo - cambiar color principal:
```css
/* Busca esto: */
background: #DC143C;

/* Cambialo por otro color: */
background: #2196F3;  /* Azul */
```

### Agregar nuevas tarjetas de opciones
Edita: `index.html`

Busca la seccion `options-grid` y agrega:
```html
<div class="option-card" onclick="setQuery('Tu pregunta aqui')">
    <div class="icon">🎓</div>
    <h3>Nuevo Titulo</h3>
    <p>Descripcion</p>
</div>
```

### Cambiar el comportamiento de la IA
Edita: `app.py`

Busca `SYSTEM_PROMPT` y modificalo:
```python
SYSTEM_PROMPT = """
Eres un asistente que habla como pirata.
Siempre termina tus respuestas con "¡Arrr!"
"""
```

### Cambiar el modelo de IA
En `app.py`:
```python
# Cambiar de gemini-2.5-flash a gemini-2.5-pro
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",  # Mas potente
    ...
)
```

## PARTE 6: Conceptos clave explicados

### HTTP Request/Response
```
Frontend: "Hola backend, tengo esta pregunta"
Backend: "Ok, aqui esta la respuesta de la IA"
```

### API (Application Programming Interface)
Una forma de que dos programas hablen entre si.

En nuestro caso:
- Frontend habla con Backend via API
- Backend habla con Gemini via API

### CORS (Cross-Origin Resource Sharing)
Permiso para que el frontend (puerto 8080) hable con el backend (puerto 5000).

Sin CORS = "Error: Blocked by CORS policy"

### JSON (JavaScript Object Notation)
Formato para intercambiar datos:
```json
{
  "message": "Hola",
  "response": "Hola! ¿En que puedo ayudarte?"
}
```

### Flask
Framework de Python para crear servidores web facilmente.

```python
@app.route('/chat', methods=['POST'])
def chat():
    # Aqui manejas las peticiones
```

## PARTE 7: Troubleshooting

**Error: "No se puede conectar con el backend"**
- Verifica que `app.py` este corriendo
- Abre http://localhost:5000/health en el navegador
- Deberia decir: `{"status": "ok"}`

**Error: "CORS policy"**
- Verifica que `flask-cors` este instalado
- `pip install flask-cors`

**Error: "Module not found"**
- Activa el entorno virtual
- Reinstala dependencias: `pip install -r requirements_web.txt`

**Docker no inicia**
- Verifica que Docker Desktop este corriendo
- Mira el icono en la barra de tareas

**La IA no responde**
- Verifica `config_gemini.txt` con tu API key
- Revisa la consola del backend para errores

## PARTE 8: Proximos pasos

### Nivel Basico:
1. Cambia colores y textos
2. Agrega mas tarjetas de opciones
3. Modifica el SYSTEM_PROMPT

### Nivel Intermedio:
4. Agrega un boton para limpiar historial
5. Muestra indicador de "escribiendo..."
6. Guarda conversaciones en archivos

### Nivel Avanzado:
7. Conecta a una base de datos (SQLite)
8. Agrega autenticacion de usuarios
9. Despliega en internet (Heroku, Railway, etc.)

## RECURSOS DE APRENDIZAJE

### HTML/CSS/JS:
- MDN Web Docs: https://developer.mozilla.org/es/
- FreeCodeCamp: https://www.freecodecamp.org/

### Python/Flask:
- Flask Mega Tutorial: https://blog.miguelgrinberg.com/
- Python.org: https://docs.python.org/es/

### Docker:
- Docker Get Started: https://docs.docker.com/get-started/
- Docker para principiantes (video): busca en YouTube

## ¿PREGUNTAS?

Experimenta, rompe cosas, arreglalas. Asi se aprende!
