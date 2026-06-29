from config.database import obtener_conexion
from models.usuario_entity import Usuario

class UsuarioRepository:
    
    def obtener_todos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM usuarios")
        datos = cursor.fetchall()
        cursor.close()
        conexion.close()
        
        # Transformamos los datos crudos (tuplas) en objetos Entity
        return [Usuario(fila[0], fila[1]) for fila in datos]

    def obtener_por_id(self, id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM usuarios WHERE id=%s", (id,))
        dato = cursor.fetchone()
        cursor.close()
        conexion.close()
        
        if dato:
            return Usuario(dato[0], dato[1])
        return None

    def crear(self, nombre):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO usuarios(nombre) VALUES(%s) RETURNING id', (nombre,))
        nuevo_id = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return nuevo_id

    def actualizar(self, id, nombre):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('UPDATE usuarios SET nombre=%s WHERE id=%s', (nombre, id))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id=%s', (id,))
        conexion.commit()
        cursor.close()
        conexion.close()