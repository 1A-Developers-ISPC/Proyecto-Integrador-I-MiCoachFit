# gestor_usuarios.py
import re
from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None

    def registrar_usuario(self, nombre, apellido, nombre_usuario, telefono, email, contrasena, rol='usuario'):
        if not nombre.strip():
            print("❌ El nombre no puede estar vacío.")
            return
        if not apellido.strip():
            print("❌ El apellido no puede estar vacío.")
            return
        if self.buscar_usuario(nombre_usuario):
            print("❌ El nombre de usuario ya existe.")
            return
        if not re.fullmatch(r'\d{7,15}', telefono):
            print("❌ Teléfono inválido.")
            return
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("❌ Email inválido.")
            return
        if len(contrasena) < 6 or not re.search(r'[A-Za-z]', contrasena) or not re.search(r'\d', contrasena):
            print("❌ Contraseña débil.")
            return

        nuevo = Usuario(nombre, apellido, nombre_usuario, telefono, email, contrasena, rol)
        self.usuarios.append(nuevo)
        print("✅ Usuario registrado con éxito.")

    def eliminar_usuario(self, nombre_usuario):
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            print("✅ Usuario eliminado.")
        else:
            print("❌ Usuario no encontrado.")

    def cambiar_rol(self, nombre_usuario, nuevo_rol):
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario and nuevo_rol in ['admin', 'usuario']:
            usuario.rol = nuevo_rol
            print("✅ Rol actualizado.")
        else:
            print("❌ Error al cambiar el rol.")

    def mostrar_usuarios(self):
        print("📋 Lista de usuarios:")
        for usuario in self.usuarios:
            print(f" - {usuario}")