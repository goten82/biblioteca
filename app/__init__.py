from flask import Flask
from app.models.models import db  # Importiamo l'istanza di SQLAlchemy
import secrets



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    __version__ = "0.1.0"


    # Configurazione del database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/biblioteca?options=-csearch_path=biblioteca'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inizializza il database con l'app
    db.init_app(app)
    
   


    # Importa e registra le route
    from app.routes.routes import main
    from app.routes.libri import libri_bp
    app.register_blueprint(main)
    app.register_blueprint(libri_bp)


    return app
