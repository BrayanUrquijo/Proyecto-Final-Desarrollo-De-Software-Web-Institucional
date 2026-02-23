"""
Backend Flask para Sistema Academico con IA
Sirve las paginas HTML, maneja autenticacion y chat con Gemini
"""

# ============ IMPORTS ============
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# ============ CONFIGURACION ============

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'clave-por-defecto')
CORS(app)

# ============ API KEYS ============

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    print("=" * 60)
    print("ERROR: No se encontro GEMINI_API_KEY en el archivo .env")
    print("Crea un archivo .env con: GEMINI_API_KEY=tu_api_key")
    print("=" * 60)
    exit(1)

# ============ INICIALIZAR GEMINI ============

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7,
    max_output_tokens=2048
)

# ============ SYSTEM PROMPT ============

SYSTEM_PROMPT = """
Eres un asistente virtual académico de una universidad.

Tu función es brindar apoyo a estudiantes en temas académicos y administrativos, incluyendo:
- Calificaciones
- Admisión y matrícula
- Certificados y documentos
- Horarios
- Información institucional
- Dudas administrativas

ESTILO DE RESPUESTA
Debes responder siempre con:
- Lenguaje claro, organizado y bien estructurado
- Listas con viñetas cuando enumeres información
- Redacción profesional, amable y respetuosa
- Respuestas concisas pero útiles
- Sin emojis
- Sin exageraciones ni lenguaje informal

COMPORTAMIENTO
- No inventes información.
- Si no sabes algo, dilo honestamente y recomienda contactar con la oficina correspondiente.
- No especules ni asumas datos.
- Prioriza siempre la comprensión del mensaje del usuario antes de responder.
- Si la solicitud es ambigua, pide aclaración antes de responder.

SALUD MENTAL Y BIENESTAR
Si un usuario expresa tristeza, ansiedad, angustia, estrés severo, desesperación o malestar emocional:
- Responde con empatía y respeto.
- Recomienda buscar apoyo institucional.
- Sugiere contactar servicios de bienestar universitario o apoyo psicológico.
- Mantén tono calmado y contenedor.
- Nunca minimices emociones.
- Nunca diagnostiques.

ROL
- No salgas del rol de asistente académico universitario.
- No opines fuera del ámbito académico-administrativo.
- No respondas temas ajenos a la universidad salvo que estén relacionados con bienestar estudiantil.

FORMATO
Cuando presentes opciones, servicios o pasos:
- Usa viñetas ●
- Ordena la información por prioridad o relevancia
- Evita párrafos largos innecesarios

OBJETIVO PRINCIPAL
Ayudar al estudiante de la forma más clara, útil y profesional posible, priorizando siempre su bienestar y orientación correcta dentro de la universidad.
"""


# ============ DATOS TEMPORALES (migrar a PostgreSQL en futuro) ============

# Usuarios validos (en produccion, usar base de datos)
USUARIOS_VALIDOS = {
    "2459407-3743": "admin123",
    "estudiante": "pass123",
    "demo": "demo"
}

# Historial de conversaciones en memoria
conversaciones = {}

# ============ RUTAS DE PAGINAS HTML ============

@app.route('/')
def index():
    """Ruta principal - redirige al login"""
    return redirect(url_for('login'))

@app.route('/login')
def login():
    """Pagina de login"""
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Pagina del dashboard - requiere autenticacion"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])

# ============ API - AUTENTICACION ============

@app.route('/api/login', methods=['POST'])
def api_login():
    """Endpoint para autenticacion"""
    try:
        data = request.json
        username = data.get('username', '')
        password = data.get('password', '')
        
        if username in USUARIOS_VALIDOS and USUARIOS_VALIDOS[username] == password:
            session['user'] = username
            return jsonify({
                "success": True,
                "message": "Login exitoso",
                "username": username
            })
        else:
            return jsonify({
                "success": False,
                "message": "Usuario o contrasena incorrectos"
            }), 401
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

@app.route('/api/logout', methods=['POST'])
def api_logout():
    """Endpoint para cerrar sesion"""
    session.pop('user', None)
    return jsonify({"success": True, "message": "Sesion cerrada"})

@app.route('/api/check-session', methods=['GET'])
def check_session():
    """Verificar si hay sesion activa"""
    if 'user' in session:
        return jsonify({
            "logged_in": True,
            "username": session['user']
        })
    return jsonify({"logged_in": False})

# ============ API - CHAT CON IA ============

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint para el chat con IA"""
    try:
        if 'user' not in session:
            return jsonify({"error": "No autenticado"}), 401
        
        data = request.json
        mensaje_usuario = data.get('message', '')
        session_id = session.get('user', 'default')
        
        if not mensaje_usuario:
            return jsonify({"error": "Mensaje vacio"}), 400
        
        # Obtener historial
        if session_id not in conversaciones:
            conversaciones[session_id] = []
        
        historial = conversaciones[session_id]
        
        # Preparar mensajes
        mensajes = [SystemMessage(content=SYSTEM_PROMPT)]
        mensajes.extend(historial)
        mensajes.append(HumanMessage(content=mensaje_usuario))
        
        # Obtener respuesta de Gemini
        respuesta = llm.invoke(mensajes)
        texto_respuesta = respuesta.content

        # Guardar en historial
        historial.append(HumanMessage(content=mensaje_usuario))
        historial.append(AIMessage(content=texto_respuesta))
        
        # Limitar historial a 20 mensajes
        if len(historial) > 20:
            historial = historial[-20:]
        
        conversaciones[session_id] = historial
        
        return jsonify({
            "response": texto_respuesta,
            "session_id": session_id
        })
        
    except Exception as e:
        print(f"Error en chat: {e}")
        return jsonify({
            "error": "Error al procesar la solicitud",
            "details": str(e)
        }), 500

@app.route('/api/clear-chat', methods=['POST'])
def clear_chat():
    """Limpiar historial de chat"""
    try:
        if 'user' not in session:
            return jsonify({"error": "No autenticado"}), 401
        
        session_id = session.get('user', 'default')
        if session_id in conversaciones:
            conversaciones[session_id] = []
        
        return jsonify({"message": "Historial limpiado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============ API - UTILIDADES ============

@app.route('/health', methods=['GET'])
def health():
    """Verificar que el servidor esta corriendo"""
    return jsonify({"status": "ok", "message": "Backend funcionando correctamente"})

# ============ INICIAR SERVIDOR ============

if __name__ == '__main__':
    print("=" * 60)
    print("Servidor Flask iniciado")
    print("Accede a: http://localhost:5000")
    print("=" * 60)
    print("\nCredenciales de prueba:")
    print("- Usuario: 2459407-3743 | Password: admin123")
    print("- Usuario: estudiante | Password: pass123")
    print("- Usuario: demo | Password: demo")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)