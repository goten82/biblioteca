from flask import Blueprint,render_template
from flask_login import LoginManager, login_required, current_user

# Creiamo un blueprint per le rotte principali
main = Blueprint('main', __name__)

login_manager = LoginManager()
login_manager.login_view = "bibliotecari.login" 

@main.route('/')
def home():
    return "Benvenuto nella mia app Flask con PostgreSQL!"

@main.route('/home')
def form():
    return render_template('form.html')
