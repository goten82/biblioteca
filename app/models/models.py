from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Libri(db.Model):
    __tablename__ = 'libri'
    id_libri = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(15), unique=True, nullable=False)
    anno_pubblicazione = db.Column(db.Integer)
    copie_disponibili = db.Column(db.Integer, default=1)
    id_autore = db.Column(db.Integer, db.ForeignKey('autori.id_autori'), nullable=False)
    prestiti = db.relationship('Prestiti', backref='libro', lazy=True)

class Autori(db.Model):
    __tablename__ = 'autori'
    id_autori = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    libri = db.relationship('Libri', backref='autore', lazy=True)

class Bibliotecari(db.Model):
    __tablename__ = 'bibliotecari'
    id_bibliotecari = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password= db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Prestiti(db.Model):
    __tablename__ = 'prestiti'
    id_prestiti = db.Column(db.Integer, primary_key=True)
    data_prestito = db.Column(db.DateTime, nullable=False)
    data_restituzione = db.Column(db.DateTime)
    id_libri = db.Column(db.Integer, db.ForeignKey('libri.id_libri'), nullable=False)
    id_utenti = db.Column(db.Integer, db.ForeignKey('utenti.id_utenti'), nullable=False)
    
class Utenti(db.Model):
    __tablename__ = 'utenti'
    id_utenti = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    prestiti = db.relationship('Prestiti', backref='utente', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
