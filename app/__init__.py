from flask import Flask,session,redirect,url_for,flash
from app.models.models import db  # Importiamo l'istanza di SQLAlchemy
import secrets
from functools import wraps
from flask_login import LoginManager, login_required, current_user
import os



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    __version__ = "0.1.3"


    # Configurazione del database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/biblioteca?options=-csearch_path=biblioteca'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)  # Chiave segreta per la sessione

    # Inizializza il database con l'app
    db.init_app(app)

    # Importa e registra le route
    from app.routes.routes import main
    from app.routes.libri import libri_bp
    from app.routes.bibliotecari import bibliotecari_bp
    from app.routes.auth import auth_bp
    app.register_blueprint(main)
    app.register_blueprint(libri_bp)
    app.register_blueprint(bibliotecari_bp)
    app.register_blueprint(auth_bp)

   
    return app
