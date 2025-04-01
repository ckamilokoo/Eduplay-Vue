from flask import Flask
from flask_cors import CORS
from app.rutas.rutas import main_bp
from app.modelo.sql import db  # Importa tu base de datos desde el archivo correspondiente

import os 
from dotenv import load_dotenv
import base64


# Cargar las variables de entorno desde el archivo .env
load_dotenv()


class ServerConfig:

    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    app.config.from_object(ServerConfig)
    
    

    # Inicializa SQLAlchemy con la aplicación
    db.init_app(app)
    
   

    # Configura CORS para permitir solicitudes desde cualquier origen
    CORS(app)

    app.register_blueprint(main_bp, url_prefix='/')
    
    return app