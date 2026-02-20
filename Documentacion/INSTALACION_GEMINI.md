# INSTALACION - GOOGLE GEMINI

## Pasos para configurar el proyecto con Gemini

### 1. Crear entorno virtual
```powershell
python -m venv .venv
```

### 2. Activar entorno virtual
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```powershell
pip install langchain langchain-google-genai google-generativeai
```

### 4. Configurar API key
Tu API key ya esta en `config_gemini.txt`:
```
AIzaSyCjoAvYgQPnr8VJVl_pUxKTiUfFeRKDPPI
```

### 5. Ejecutar el chat
```powershell
python chat_gemini_auto.py
```

## Modelos de Gemini disponibles

- `gemini-1.5-flash` (Rapido, gratuito) ✅ DEFAULT
- `gemini-1.5-pro` (Mas potente, tambien gratuito)
- `gemini-pro` (Version anterior)

### Para cambiar el modelo:
Edita en `chat_gemini_auto.py`:
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Cambia aqui
    ...
)
```

## Limites del plan gratuito de Gemini

- **gemini-1.5-flash**: 15 RPM (requests per minute), 1M TPM (tokens per minute)
- **gemini-1.5-pro**: 2 RPM, 32K TPM
- Sin expiracion
- Sin tarjeta de credito requerida

## Comandos del chat

- `salir` / `exit` - Cerrar el chat
- `limpiar` - Borrar historial de conversacion
- Cualquier otra cosa - Pregunta normal al bot

## Comparacion: Gemini vs Groq

| Caracteristica | Gemini | Groq |
|---------------|---------|------|
| Velocidad | Media | Muy rapida |
| Calidad | Excelente | Excelente |
| Limite gratuito | Generoso | Muy generoso |
| Modelos | Google | Meta (Llama), Mixtral |
| Multimodal | Si (imagenes) | No |

Ambos son excelentes opciones gratuitas!

## Troubleshooting

**Error: "API key not valid"**
- Verifica que tu API key este correcta en `config_gemini.txt`
- Asegurate de no tener espacios extras

**Error: "quota exceeded"**
- Has alcanzado el limite de requests por minuto
- Espera 1 minuto y vuelve a intentar

**Error: "module not found"**
- Asegurate de tener el entorno virtual activado
- Reinstala: `pip install langchain-google-genai`
