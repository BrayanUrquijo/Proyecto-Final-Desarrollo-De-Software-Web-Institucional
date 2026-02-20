// URL del backend (cambiar segun donde este corriendo)
const API_URL = 'http://localhost:5000';

// Funcion para establecer una pregunta predefinida
function setQuery(question) {
    document.getElementById('userInput').value = question;
    document.getElementById('userInput').focus();
}

// Funcion para manejar Enter en el input
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

// Funcion principal para enviar mensaje
async function sendMessage() {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Mostrar mensaje del usuario
    addMessage(message, 'user');
    
    // Limpiar input
    input.value = '';
    
    // Mostrar loading
    showLoading(true);
    
    try {
        // Llamar al backend
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        
        const data = await response.json();
        
        // Mostrar respuesta del bot
        addMessage(data.response, 'bot');
        
    } catch (error) {
        console.error('Error:', error);
        addMessage('Lo siento, hubo un error al procesar tu pregunta. Intenta de nuevo.', 'bot');
    } finally {
        showLoading(false);
    }
}

// Funcion para agregar mensaje al chat
function addMessage(text, sender) {
    const messagesContainer = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    
    messageDiv.className = `message ${sender === 'user' ? 'user-message' : 'bot-message'}`;
    
    if (sender === 'user') {
        messageDiv.innerHTML = `<strong>Tu:</strong> ${text}`;
    } else {
        messageDiv.innerHTML = `<strong>Asistente IA:</strong> ${text}`;
    }
    
    messagesContainer.appendChild(messageDiv);
    
    // Scroll automatico al final
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Funcion para mostrar/ocultar loading
function showLoading(show) {
    const loading = document.getElementById('loading');
    loading.style.display = show ? 'block' : 'none';
}

// Verificar conexion con el backend al cargar la pagina
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (response.ok) {
            console.log('Conexion con backend exitosa');
        }
    } catch (error) {
        console.warn('No se pudo conectar con el backend:', error);
        addMessage('Advertencia: No hay conexion con el servidor. Asegurate de que el backend este corriendo.', 'bot');
    }
});
