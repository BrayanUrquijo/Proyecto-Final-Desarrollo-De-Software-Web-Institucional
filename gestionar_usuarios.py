from app import app, db, Usuario, Mensaje
import sys

def print_menu():
    print("\n" + "="*35)
    print(" 🛠️  PANEL DE GESTIÓN DE USUARIOS 🛠️ ")
    print("="*35)
    print("1. ➕ Crear nuevo usuario")
    print("2. ✏️  Modificar usuario (Nombre/Contraseña)")
    print("3. ❌ Eliminar usuario")
    print("4. 📋 Listar todos los usuarios")
    print("5. 🚪 Salir")
    return input("Seleccione una opción (1-5): ")

def crear_usuario():
    print("\n--- CREAR USUARIO ---")
    username = input("Ingrese el nombre de usuario (ej. est123): ").strip()
    if not username:
        print("❌ El nombre de usuario no puede estar vacío.")
        return
        
    password = input("Ingrese la contraseña: ").strip()
    
    with app.app_context():
        if Usuario.query.filter_by(username=username).first():
            print(f"❌ El usuario '{username}' ya existe.")
            return
            
        nuevo_usuario = Usuario(username=username, password_hash=password)
        db.session.add(nuevo_usuario)
        try:
            db.session.commit()
            print(f"✅ ¡Usuario '{username}' creado exitosamente!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error al crear usuario: {e}")

def modificar_usuario():
    print("\n--- MODIFICAR USUARIO ---")
    username_actual = input("Ingrese el nombre del usuario a modificar: ").strip()
    
    with app.app_context():
        usuario = Usuario.query.filter_by(username=username_actual).first()
        if not usuario:
            print(f"❌ El usuario '{username_actual}' no existe.")
            return
            
        print("Deje el espacio en blanco y presione ENTER si no desea cambiar el valor.")
        nuevo_username = input(f"Nuevo nombre de usuario [{username_actual}]: ").strip()
        nueva_password = input("Nueva contraseña [***]: ").strip()
        
        hubo_cambios = False
        
        if nuevo_username and nuevo_username != username_actual:
            if Usuario.query.filter_by(username=nuevo_username).first():
                print(f"❌ No se puede usar '{nuevo_username}', ya está ocupado por otro usuario.")
                return
            usuario.username = nuevo_username
            hubo_cambios = True
            
        if nueva_password:
            usuario.password_hash = nueva_password
            hubo_cambios = True
            
        if hubo_cambios:
            try:
                db.session.commit()
                print(f"✅ ¡Usuario modificado exitosamente!")
            except Exception as e:
                db.session.rollback()
                print(f"❌ Error al modificar usuario: {e}")
        else:
            print("⚠️ No se realizaron cambios.")

def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    username = input("Ingrese el nombre del usuario a eliminar: ").strip()
    
    with app.app_context():
        usuario = Usuario.query.filter_by(username=username).first()
        if not usuario:
            print(f"❌ El usuario '{username}' no existe.")
            return
            
        confirmacion = input(f"⚠️ ¿Está seguro que desea eliminar a '{username}'? Esta acción no se puede deshacer. (s/n): ").strip().lower()
        if confirmacion == 's':
            # Primero eliminamos el historial de chat para evitar el error de Restricción de Llave Foránea (Foreign Key)
            Mensaje.query.filter_by(session_id=username).delete()
            
            # Ahora sí eliminamos al usuario
            db.session.delete(usuario)
            try:
                db.session.commit()
                print(f"✅ ¡Usuario '{username}' eliminado exitosamente!")
            except Exception as e:
                db.session.rollback()
                print(f"❌ Error al eliminar usuario: {e}")
        else:
            print("Acción cancelada.")

def listar_usuarios():
    print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
    with app.app_context():
        usuarios = Usuario.query.all()
        if not usuarios:
            print("No hay usuarios registrados actualmente.")
            return
            
        print(f"Total de usuarios: {len(usuarios)}")
        print("-" * 30)
        for u in usuarios:
            print(f"👤 Username: {u.username}")
        print("-" * 30)

def main():
    while True:
        try:
            opcion = print_menu()
            if opcion == '1':
                crear_usuario()
            elif opcion == '2':
                modificar_usuario()
            elif opcion == '3':
                eliminar_usuario()
            elif opcion == '4':
                listar_usuarios()
            elif opcion == '5':
                print("Saliendo del gestor de usuarios...")
                sys.exit(0)
            else:
                print("❌ Opción inválida. Seleccione un número del 1 al 5.")
        except KeyboardInterrupt:
            print("\nSaliendo del gestor de usuarios...")
            sys.exit(0)

if __name__ == '__main__':
    main()