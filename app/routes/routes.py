from flask import Blueprint,render_template
from flask_login import LoginManager
from app.routes.bibliotecari import login_required

# Creiamo un blueprint per le rotte principali
main = Blueprint('main', __name__)

login_manager = LoginManager()
login_manager.login_view = "bibliotecari.login" 

@main.route('/')
@login_required
def home():
    return "Benvenuto nella mia app Flask con PostgreSQL!"

@main.route('/home')
def form():
    return render_template('form.html')
