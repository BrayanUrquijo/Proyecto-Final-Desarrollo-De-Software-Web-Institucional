"""
Backend Flask para Sistema Academico con IA
Ahora sirve las paginas HTML y maneja autenticacion
"""

from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'tu-clave-secreta-super-segura-cambiar-en-produccion'  # CAMBIAR en produccion
CORS(app)

# Cargar API key
def cargar_api_key():
    try:
        with open('config_gemini.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("ERROR: No se encontro config_gemini.txt")
        return None

# Inicializar Gemini
api_key = cargar_api_key()
if not api_key:
    print("ERROR: No se pudo cargar la API key")
    exit(1)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.7,
    max_output_tokens=2048
)

# System prompt
SYSTEM_PROMPT = """
Eres un asistente virtual para un sistema academico universitario.
Ayudas a estudiantes con:
- Consultas sobre calificaciones
- Proceso de admision y matricula
- Solicitud de certificados y documentos
- Horarios de clase
- Informacion de contacto
- Resolucion de dudas administrativas

Responde de forma amable, clara y profesional.
Si no sabes algo, sugiere contactar con la oficina de registro academico.
"""

# Usuarios validos (en produccion, usar base de datos)
USUARIOS_VALIDOS = {
    "2459407-3743": "admin123",
    "estudiante": "pass123",
    "demo": "demo"
}

# Historial de conversaciones
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

# ============ RUTAS DE API ============

@app.route('/api/login', methods=['POST'])
def api_login():
    """Endpoint para autenticacion"""
    try:
        data = request.json
        username = data.get('username', '')
        password = data.get('password', '')
        
        # Verificar credenciales
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

@app.route('/health', methods=['GET'])
def health():
    """Verificar que el servidor esta corriendo"""
    return jsonify({"status": "ok", "message": "Backend funcionando correctamente"})

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint para el chat con IA"""
    try:
        # Verificar sesion
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
        
        # Limitar historial
        if len(historial) > 20:
            historial = historial[-20:]
        
        conversaciones[session_id] = historial
        
        return jsonify({
            "response": texto_respuesta,
            "session_id": session_id
        })
        
    except Exception as e:
        print(f"Error: {e}")
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