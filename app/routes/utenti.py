from flask import Blueprint,render_template
from app.models.models import Utenti
from app.decorators import login_required  


utenti_bp = Blueprint('utenti', __name__)

@utenti_bp.route('/utenti',methods=['GET'])
@login_required
def interfaccia():
    bib = Utenti.query.all()
    return render_template('bibliotecari.html', bibliotecari=bib)

