"""
Backend Flask para Sistema Academico con IA
Conecta el frontend con Google Gemini
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el frontend

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

# System prompt para el contexto academico
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

# Historial de conversaciones (en produccion usar base de datos)
conversaciones = {}

@app.route('/health', methods=['GET'])
def health():
    """Endpoint para verificar que el servidor esta corriendo"""
    return jsonify({"status": "ok", "message": "Backend funcionando correctamente"})

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint principal para el chat"""
    try:
        data = request.json
        mensaje_usuario = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not mensaje_usuario:
            return jsonify({"error": "Mensaje vacio"}), 400
        
        # Obtener historial de la sesion
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
        
        # Limitar historial a ultimas 10 interacciones
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

@app.route('/clear', methods=['POST'])
def clear_history():
    """Endpoint para limpiar historial de conversacion"""
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        if session_id in conversaciones:
            conversaciones[session_id] = []
        
        return jsonify({"message": "Historial limpiado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Servidor Flask iniciado")
    print("Backend corriendo en: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
