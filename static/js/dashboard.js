// Dashboard - Chat con IA

// Funciones del chat
function setQuery(question) {
    document.getElementById('userInput').value = question;
    document.getElementById('userInput').focus();
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

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
        const response = await fetch('/api/chat', {
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
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function showLoading(show) {
    const loading = document.getElementById('loading');
    loading.style.display = show ? 'block' : 'none';
}

// Funcion para cerrar sesion
async function logout() {
    if (confirm('¿Estas seguro de que quieres cerrar sesion?')) {
        try {
            await fetch('/api/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            window.location.href = '/login';
        } catch (error) {
            console.error('Error al cerrar sesion:', error);
            window.location.href = '/login';
        }
    }
}

// Verificar conexion al cargar
window.addEventListener('load', async () => {
    try {
        const response = await fetch('/health');
        if (response.ok) {
            console.log('Conexion con backend exitosa');
        }
    } catch (error) {
        console.warn('Error de conexion:', error);
    }
});