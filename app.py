from flask import Flask
from controllers.usuario_controller import usuario_bp

app = Flask(__name__)

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    print("Iniciando servidor con arquitectura por capas...")
    app.run(debug=True)