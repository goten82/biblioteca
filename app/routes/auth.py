from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.models import Bibliotecari,db
import re

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Controlla se il bibliotecario esiste nel DB
        bibliotecario = Bibliotecari.query.filter_by(username=username).first()

        if bibliotecario and bibliotecario.check_password(password):
            session['bibliotecario_id'] = bibliotecario.id_bibliotecari # Salva l'ID nella sessione
            session['bibliotecario_nome'] = bibliotecario.nome  # Salva il nome nella sessione
            session['bibliotecario_cognome'] = bibliotecario.cognome  # Salva il cognome nella sessione
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('main.form'))  # Reindirizza alla dashboard

        flash('Username o password errati', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('bibliotecario_id', None)  # Rimuove l'ID dalla sessione
    session.pop('bibliotecario_nome', None) # Rimuove il nome dalla sessione
    session.pop('bibliotecario_cognome', None) # Rimuove il cognome dalla sessione
    flash('Logout effettuato con successo!', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        username = request.form.get('username')
        password = request.form.get('password')

        # Verifica se il bibliotecario con lo stesso username esiste già
        if Bibliotecari.query.filter_by(username=username).first():
            flash('Username già in uso, scegli un altro username.', 'danger')
            return redirect(url_for('auth.register'))
        # Controllo sicurezza password
        error = is_password_secure(password)
        if error:
            flash(error, "danger")
            return redirect(url_for("utenti.register"))
        
        # Creazione del nuovo bibliotecario
        nuovo_bibliotecario = Bibliotecari(
            nome=nome,
            cognome=cognome,
            username=username
        )
        nuovo_bibliotecario.set_password(password)

        db.session.add(nuovo_bibliotecario)
        db.session.commit()

        flash('Registrazione completata! Ora puoi effettuare il login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

def is_password_secure(password):
    """Verifica se la password rispetta i criteri di sicurezza."""
    if len(password) < 8:
        return "La password deve avere almeno 8 caratteri."
    if not re.search(r'[A-Z]', password):
        return "La password deve contenere almeno una lettera maiuscola."
    if not re.search(r'[a-z]', password):
        return "La password deve contenere almeno una lettera minuscola."
    if not re.search(r'[0-9]', password):
        return "La password deve contenere almeno un numero."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "La password deve contenere almeno un carattere speciale (!@#$%^&*)."
    
    return None  # Nessun errore, password valida
