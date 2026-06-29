class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    # Método de ayuda para convertir el objeto a un diccionario (útil para JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }