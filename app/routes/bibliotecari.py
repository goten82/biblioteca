from flask import Blueprint,render_template
from app.models.models import Bibliotecari
from app.decorators import login_required  


bibliotecari_bp = Blueprint('bibliotecari', __name__)

@bibliotecari_bp.route('/bibliotecari',methods=['GET'])
@login_required
def interfaccia():
    bib = Bibliotecari.query.all()
    return render_template('bibliotecari.html', bibliotecari=bib)

