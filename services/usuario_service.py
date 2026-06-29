from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def obtener_usuarios(self):
        usuarios_entities = self.repository.obtener_todos()
        # Convertimos las Entities a diccionarios para el Controller
        return [usuario.to_dict() for usuario in usuarios_entities]

    def obtener_usuario(self, id):
        usuario = self.repository.obtener_por_id(id)
        if usuario:
            return usuario.to_dict(), 200
        return {"error": "Usuario no encontrado"}, 404

    def crear_usuario(self, datos):
        if 'nombre' not in datos or not datos['nombre']:
            return {"error": "El nombre es obligatorio"}, 400
            
        nuevo_id = self.repository.crear(datos['nombre'])
        return {"id": nuevo_id, "nombre": datos['nombre']}, 201

    def actualizar_usuario(self, id, datos):
        # Validaciones de negocio
        usuario_existente = self.repository.obtener_por_id(id)
        if not usuario_existente:
            return {"error": "Usuario no encontrado"}, 404
            
        self.repository.actualizar(id, datos['nombre'])
        return {"mensaje": "Usuario actualizado correctamente"}, 200

    def eliminar_usuario(self, id):
        usuario_existente = self.repository.obtener_por_id(id)
        if not usuario_existente:
            return {"error": "Usuario no encontrado"}, 404
            
        self.repository.eliminar(id)
        return {"mensaje": "Usuario eliminado correctamente"}, 200