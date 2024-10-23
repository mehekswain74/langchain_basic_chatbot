from flask import Flask
from app.routes import bp
from constants import openai_key
import os

os.environ["OPENAI_API_KEY"] = openai_key

# Ensure OpenAI API key is set
if 'OPENAI_API_KEY' not in os.environ:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
