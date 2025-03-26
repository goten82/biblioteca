from flask import Blueprint,render_template,request,flash,redirect,url_for
from sqlalchemy import null
from app.models.models import Libri,db

libri_bp = Blueprint('libri', __name__)

@libri_bp.route('/libri',methods=['GET'])
def get_libri():
    libri = Libri.query.all()
    return render_template('libri.html',libri=libri)

@libri_bp.route('/inserisci_libro',methods=['GET'])
def inserisci_libro():
    return render_template('gestione_libro.html',libro=None)

@libri_bp.route('/inserisci_libro',methods=['POST'])
def insert_libro():
    
    titolo=request.form['titolo'] 
   
    isbn=request.form['isbn'] 
    anno_pubblicazione=request.form['anno_pubblicazione'] 
    copie_disponibili=request.form['copie_disponibili']

    id_autore = request.form.get('id_autore', None)

    # Converti id_autore in intero solo se è un valore valido
    if id_autore:
        id_autore = int(id_autore)  # Converte solo se non è vuoto
    else:
        id_autore = None  # Evita di passare una stringa vuota a PostgreSQL

    new_libro = Libri(
        titolo=titolo,
        isbn=isbn,
        anno_pubblicazione=int(anno_pubblicazione) if anno_pubblicazione else None,
        copie_disponibili=int(copie_disponibili) if copie_disponibili else 1,  # Default a 1
        id_autore=id_autore
    )

    db.session.add(new_libro)
    db.session.commit()
    flash("Libro inserito con successo!", "success")
    return redirect(url_for('libri.get_libri'))

@libri_bp.route('/modifica_libri/<int:id>',methods=['GET'])
def modifica_libri(id):
    libro = Libri.query.first_or_404(id)
    return render_template('gestione_libro.html',libro=libro)

@libri_bp.route('/modifica_libri/<int:id>',methods=['POST'])
def update_libro(id):
    libro = Libri.query.first_or_404(id) # Cerca l'utente per ID

     # Aggiorna i campi dell'utente    
    libro.titolo=request.form['titolo'] 
    libro.autore_id=request.form['id_autore']
    libro.isbn=request.form['isbn'] 
    libro.anno_pubblicazione=request.form['anno_pubblicazione'] 
    libro.copie_disponibili=request.form['copie_disponibili']

    
    db.session.commit()  # Salva le modifiche nel database
    flash("Libro aggiornato con successo!", "success")
    return redirect(url_for('libri.get_libri'))

@libri_bp.route('/elimina_libro',methods=['DELETE'])
def elimina_libro():
    pass