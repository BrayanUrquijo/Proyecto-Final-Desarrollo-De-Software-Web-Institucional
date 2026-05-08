import os

print("--- Inicialización de Base de Datos en Neon ---")
neon_url = input("Pegue su enlace DATABASE_URL de Neon aquí: ")

if neon_url.startswith("postgres://"):
    neon_url = neon_url.replace("postgres://", "postgresql://", 1)

# Sobrescribimos la variable de entorno ANTES de importar app
os.environ['DATABASE_URL'] = neon_url
os.environ['GEMINI_API_KEY'] = 'dummy_key_para_ignorar_validacion'

from app import app, db

with app.app_context():
    try:
        db.create_all()
        print("\n✅ ¡Tablas creadas exitosamente en la base de datos de Neon!")
    except Exception as e:
        print(f"\n❌ Hubo un error al crear las tablas: {e}")
