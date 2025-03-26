from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from app.models.models import Libri,Autori,db

libri_bp = Blueprint('libri', __name__)

@libri_bp.route('/libri',methods=['GET'])
def get_libri():
    libri = Libri.query.all()
    return render_template('libri.html',libri=libri)

@libri_bp.route('/inserisci_libro',methods=['GET'])
def inserisci_libro():
    autori = Autori.query.all()
    return render_template('gestione_libro.html',libro=None, autore=None,autori=autori)

@libri_bp.route('/inserisci_libro',methods=['POST'])
def insert_libro():
    
    titolo=request.form['titolo']    
    isbn=request.form['isbn'] 
    anno_pubblicazione=request.form['anno_pubblicazione'] 
    copie_disponibili=request.form['copie_disponibili']

    id_autore = request.form.get('id_autore', None)
    nome =  request.form.get('nome')
    cognome = request.form.get('cognome')
    if nome and cognome:
        autore = Autori.query.filter_by(nome=nome,cognome=cognome).first()
        if not autore:
            autore = Autori(nome=nome,cognome=cognome)
            db.session.add(autore)
            db.session.commit()
        id_autore = autore.id_autori

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
    libro = Libri.query.get_or_404(id)
    autore = Autori.query.get(libro.id_autore)
    autori = Autori.query.all()
    return render_template('gestione_libro.html',libro=libro, autore=autore,autori=autori)

@libri_bp.route('/modifica_libri/<int:id>',methods=['POST'])
def update_libro(id):
    libro = Libri.query.first_or_404(id) # Cerca l'utente per ID

     # Aggiorna i campi dell'utente    
    libro.titolo=request.form['titolo'] 
    
    libro.isbn=request.form['isbn'] 
    libro.anno_pubblicazione=request.form['anno_pubblicazione'] 
    libro.copie_disponibili=request.form['copie_disponibili']
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    if nome and cognome:
        autore = Autori.query.filter_by(nome=nome,cognome=cognome).first()
        if not autore:
            autore = Autori(nome=nome,cognome=cognome)
            db.session.add(autore)
            db.session.commit()
        id_autore = autore.id_autori

    libro.id_autore= id_autore if nome and cognome else request.form['id_autori']

    
    db.session.commit()  # Salva le modifiche nel database
    flash("Libro aggiornato con successo!", "success")
    return redirect(url_for('libri.get_libri'))

@libri_bp.route('/elimina_libro/<int:id>',methods=['DELETE'])
def elimina_libro(id):
    libro = Libri.query.get_or_404(id)
    db.session.delete(libro)  # Elimina l'utente dal database
    db.session.commit()
    return jsonify({"message": "Libro eliminato con successo!"})

@libri_bp.route('/cerca',methods=['GET'])
def cerca():
    return render_template('cerca.html')

@libri_bp.route('/find',methods=['GET'])
def find():
    to_research = request.args['ricerca']
    tipoRicerca = request.args['flexRadioDefault']
    
    if(tipoRicerca=='titolo'):
        libri = Libri.query.filter(Libri.titolo.ilike(f"%{to_research}%")).all()
    # else:
    #     libri = Libri.query.filter(Libri.autore.ilike(f"%{to_research}%")).all()
    
    return render_template('libri.html',libri=libri)