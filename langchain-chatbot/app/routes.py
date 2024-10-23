from flask import Blueprint, request, jsonify, render_template
from flask_restful import Api, Resource
from .chatbot import Chatbot

bp = Blueprint('main', __name__)
api = Api(bp)

chatbot = Chatbot()

@bp.route('/')
def home():
    return render_template('index.html')

class ChatResource(Resource):
    def get(self):
        return jsonify({'message': 'Please send a POST request with a query parameter to chat.'})

    def post(self):
        data = request.get_json()
        query = data.get('query')
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        response = chatbot.get_response(query)
        return jsonify({'response': response})

api.add_resource(ChatResource, '/chat')
