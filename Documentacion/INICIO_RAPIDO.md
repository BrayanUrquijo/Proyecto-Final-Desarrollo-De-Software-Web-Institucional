# INICIO RAPIDO - 5 MINUTOS

## Opcion A: Sin Docker (Recomendado para empezar)

### 1. Preparar
```powershell
cd proyecto-web-ia
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements_web.txt
```

### 2. Iniciar Backend
```powershell
# Terminal 1
python app.py
```

### 3. Abrir Frontend
```
Doble click en index.html
```

**¡LISTO!** Ya puedes chatear con la IA.

---

## Opcion B: Con Docker (Mas facil pero requiere Docker instalado)

### 1. Instalar Docker Desktop
https://www.docker.com/products/docker-desktop/

### 2. Ejecutar
```powershell
docker-compose up --build
```

### 3. Abrir navegador
http://localhost:8080

**¡LISTO!** Todo funciona automaticamente.

---

## Verificar que funciona

1. Abre el navegador en http://localhost:8080
2. Escribe: "Hola, ¿como estas?"
3. La IA deberia responder

## Si algo falla

1. Verifica que `config_gemini.txt` tenga tu API key
2. Verifica que el backend este corriendo (puerto 5000)
3. Lee `GUIA_COMPLETA_WEB.md` para mas ayuda

## Estructura de archivos

```
proyecto-web-ia/
├── index.html              # Abre esto en el navegador
├── styles.css              # Cambia colores aqui
├── script.js               # Logica del frontend
├── app.py                  # Ejecuta esto (backend)
├── config_gemini.txt       # Pon tu API key aqui
└── requirements_web.txt    # Dependencias
```

## Comandos utiles

```powershell
# Activar entorno virtual
.venv\Scripts\Activate.ps1

# Iniciar backend
python app.py

# Ver si el backend esta corriendo
# Abre: http://localhost:5000/health

# Detener todo
Ctrl + C
```

## Personalizar

- **Colores**: Edita `styles.css`
- **Textos**: Edita `index.html`
- **Comportamiento IA**: Edita `SYSTEM_PROMPT` en `app.py`

¡Experimenta y diviertete! 🚀
