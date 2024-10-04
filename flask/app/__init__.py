from flask import Flask
from flask_cors import CORS
from app.rutas.rutas import main_bp
from app.modelo.sql import db  # Importa tu base de datos desde el archivo correspondiente

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    # Configura la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()

    # Configura CORS para permitir solicitudes desde cualquier origen
    CORS(app)

    app.register_blueprint(main_bp, url_prefix='/')
    
    return app