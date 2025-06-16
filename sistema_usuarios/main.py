# ------------------- main.py -------------------
from gestor_usuarios import GestorUsuarios
from menu_sistema import MenuSistema

def main():
    gestor = GestorUsuarios()

    # Crea un admin por defecto si no existe
    if not gestor.buscar_usuario("admin"):
        gestor.registrar_usuario(
            nombre="Admin", apellido="Master", nombre_usuario="admin",
            telefono="123456789", email="admin@ejemplo.com",
            contrasena="admin123", rol="admin"
        )

    menu = MenuSistema(gestor)
    menu.menu_principal()

if __name__ == "__main__":
    main()

