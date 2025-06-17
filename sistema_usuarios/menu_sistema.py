# ------------------- menu_sistema.py -------------------

class MenuSistema:
    def __init__(self, gestor):
        self.gestor = gestor

    def menu_principal(self):
        while True:
            print("\n=== Sistema MiCoachFit ===")
            print("1. Registrar usuario")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.menu_registro()
            elif opcion == '2':
                self.menu_login()
            elif opcion == '3':
                print("👋 Hasta luego!")
                break
            else:
                print("⚠️ Opción inválida")

    def menu_registro(self):
        print("\n--- Registro de Usuario ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        nombre_usuario = input("Nombre de usuario: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        contrasena = input("Contraseña: ")
        self.gestor.registrar_usuario(nombre, apellido, nombre_usuario, telefono, email, contrasena)

    def menu_login(self):
        print("\n--- Iniciar Sesión ---")
        nombre_usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        usuario = self.gestor.buscar_usuario(nombre_usuario)
        if usuario and usuario.verificar_credenciales(contrasena):
            print(f"🔓 Bienvenido, {usuario.nombre} ({usuario.rol})")
            if usuario.rol == 'admin':
                self.menu_admin()
            else:
                self.menu_usuario(usuario)
        else:
            print("❌ Usuario o contraseña incorrectos")

    def menu_admin(self):
        while True:
            print("\n--- Menú Admin ---")
            print("1. Ver usuarios")
            print("2. Cambiar rol")
            print("3. Eliminar usuario")
            print("4. Cerrar sesión")
            opcion = input("Opción: ")
            if opcion == '1':
                self.gestor.mostrar_usuarios()
            elif opcion == '2':
                nombre = input("Usuario: ")
                nuevo_rol = input("Nuevo rol (admin/usuario): ")
                self.gestor.cambiar_rol(nombre, nuevo_rol)
            elif opcion == '3':
                nombre = input("Usuario a eliminar: ")
                self.gestor.eliminar_usuario(nombre)
            elif opcion == '4':
                print("🔒 Sesión cerrada.")
                break
            else:
                print("⚠️ Opción inválida")

    def menu_usuario(self, usuario):
        while True:
            print(f"\n--- Menú Usuario ---")
            print("1- Mostrar Datos") 
            print("2- Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                print("--- Datos Personales de Usuario---")
                print(f"Nombre: {usuario.nombre} {usuario.apellido}")
                print(f"Teléfono: {usuario.telefono}")
                print(f"Email: {usuario.email}")
            elif opcion == "2":
                break
        print("Gracias por usar la app")


