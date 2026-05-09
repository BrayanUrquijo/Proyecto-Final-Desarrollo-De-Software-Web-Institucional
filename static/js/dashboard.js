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
        
        showLoading(false); // Ocultarlo ya que empieza el streaming
        
        // Preparar para recibir stream
        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let botText = '';
        
        // Crear elemento del mensaje del bot
        const messagesContainer = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot-message';
        const label = document.createElement('strong');
        label.textContent = 'Asistente IA: ';
        const content = document.createElement('span');
        
        messageDiv.appendChild(label);
        messageDiv.appendChild(content);
        messagesContainer.appendChild(messageDiv);
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            botText += decoder.decode(value, { stream: true });
            
            // Reemplazos de formato Markdown al vuelo
            let formattedText = botText
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>')
                .replace(/_(.*?)_/g, '<em>$1</em>')
                .replace(/(?:^|\n)\*\s/g, '<br>• ') // Reemplaza asteriscos de lista
                .replace(/(?:^|\n)-\s/g, '<br>• ')  // Reemplaza guiones de lista
                .replace(/\n/g, '<br>');
                
            content.innerHTML = formattedText;
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
    } catch (error) {
        console.error('Error:', error);
        showLoading(false);
        addMessage('Lo siento, hubo un error al procesar tu pregunta. Intenta de nuevo.', 'bot');
    }
}

function addMessage(text, sender) {
    const messagesContainer = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');

    messageDiv.className = `message ${sender === 'user' ? 'user-message' : 'bot-message'}`;

    const label = document.createElement("strong");
    label.textContent = sender === "user" ? "Tu: " : "Asistente IA: ";

    const content = document.createElement("span");
    
    if (sender === 'bot') {
        // Parsear markdown basico: Negrilla (**texto**), Cursiva (*texto* o _texto_), y saltos de linea
        let formattedText = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/_(.*?)_/g, '<em>$1</em>')
            .replace(/\n/g, '<br>');
        content.innerHTML = formattedText;
    } else {
        content.textContent = text;
    }

    messageDiv.appendChild(label);
    messageDiv.appendChild(content);

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