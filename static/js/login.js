// Login con autenticacion del backend

const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('errorMessage');

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Login exitoso
            showSuccess('Login exitoso! Redirigiendo...');
            setTimeout(() => {
                window.location.href = '/dashboard';
            }, 1000);
        } else {
            // Login fallido
            showError(data.message || 'Usuario o contraseña incorrectos');
            document.getElementById('password').value = '';
        }
    } catch (error) {
        console.error('Error:', error);
        showError('Error de conexión con el servidor');
    }
});

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.background = '#fee';
    errorMessage.style.borderColor = '#fcc';
    errorMessage.style.color = '#c00';
    
    setTimeout(() => {
        errorMessage.style.display = 'none';
    }, 3000);
}

function showSuccess(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.background = '#d4edda';
    errorMessage.style.borderColor = '#c3e6cb';
    errorMessage.style.color = '#155724';
}

function clearForm() {
    loginForm.reset();
    errorMessage.style.display = 'none';
}

// Demo: Mostrar credenciales en consola
console.log('='.repeat(50));
console.log('CREDENCIALES DE PRUEBA:');
console.log('Usuario: 2459407-3743 | Password: admin123');
console.log('Usuario: estudiante | Password: pass123');
console.log('Usuario: demo | Password: demo');
console.log('='.repeat(50));