"""
Chat con LangChain y Google Gemini - VERSION AUTOMATIZADA
API Key se lee automáticamente desde config_gemini.txt
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

def cargar_api_key():
    """Lee la API key desde el archivo config_gemini.txt"""
    try:
        with open('config_gemini.txt', 'r') as f:
            api_key = f.read().strip()
            if api_key:
                return api_key
            else:
                print("ERROR: config_gemini.txt esta vacio")
                return None
    except FileNotFoundError:
        print("ERROR: No se encontro el archivo config_gemini.txt")
        print("Crea un archivo 'config_gemini.txt' y pon tu API key de Google ahi")
        return None
    except Exception as e:
        print(f"ERROR al leer config_gemini.txt: {e}")
        return None

def main():
    print("=" * 60)
    print("CHAT CON GOOGLE GEMINI (LangChain)")
    print("=" * 60)
    
    # Cargar API key desde archivo
    api_key = cargar_api_key()
    
    if not api_key:
        print("\nNo se pudo cargar la API key. Saliendo...")
        return
    
    # Inicializar modelo Gemini
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",  # Modelo mas reciente y rapido
            google_api_key=api_key,
            temperature=0.7,
            max_output_tokens=2048
        )
        print("Conectado con modelo: gemini-2.5-flash")
    except Exception as e:
        print(f"Error al inicializar: {e}")
        print("\nVerifica que:")
        print("1. Tu API key sea valida")
        print("2. Hayas habilitado la API de Gemini en Google Cloud")
        return
    
    # Historial de conversacion
    historial = []
    
    # System prompt
    system_prompt = "Eres un asistente util y amigable. Responde de forma clara y concisa."
    
    print("\nComandos especiales:")
    print("  'salir' o 'exit' - Terminar el chat")
    print("  'limpiar' - Limpiar historial")
    print("\n" + "-" * 60 + "\n")
    
    # Loop principal
    while True:
        try:
            # Obtener pregunta
            pregunta = input("Tu: ").strip()
            
            # Comandos especiales
            if pregunta.lower() in ['salir', 'exit', 'quit']:
                print("\nHasta luego!")
                break
            
            if pregunta.lower() in ['limpiar', 'clear']:
                historial = []
                print("Historial limpiado\n")
                continue
            
            if not pregunta:
                continue
            
            # Preparar mensajes
            mensajes = [SystemMessage(content=system_prompt)]
            mensajes.extend(historial)
            mensajes.append(HumanMessage(content=pregunta))
            
            # Obtener respuesta
            print("\nGemini: ", end="", flush=True)
            respuesta = llm.invoke(mensajes)
            print(respuesta.content)
            
            # Guardar en historial
            historial.append(HumanMessage(content=pregunta))
            historial.append(AIMessage(content=respuesta.content))
            
            print("\n" + "-" * 60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nInterrumpido. Hasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()