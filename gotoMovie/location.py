from flask import Blueprint


bp = Blueprint('location', __name__, url_prefix='/location')


@bp.route('/locate', methods=['POST'])
@login_required
def locate_user():
    pass


