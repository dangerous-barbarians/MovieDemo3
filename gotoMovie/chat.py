from flask import Blueprint


bp = Blueprint('chat', __name__, url_prefix='/chat')


@bp.route('/chat-friend', methods=['POST'])
def chat_with_friend():
    pass

