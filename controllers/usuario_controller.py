from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

# Usamos Blueprint para separar las rutas del archivo principal
usuario_bp = Blueprint('usuario_controller', __name__)
service = UsuarioService()

@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    resultado = service.obtener_usuarios()
    return jsonify(resultado), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    resultado, status_code = service.obtener_usuario(id)
    return jsonify(resultado), status_code

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    resultado, status_code = service.crear_usuario(datos)
    return jsonify(resultado), status_code

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.get_json()
    resultado, status_code = service.actualizar_usuario(id, datos)
    return jsonify(resultado), status_code

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    resultado, status_code = service.eliminar_usuario(id)
    return jsonify(resultado), status_code