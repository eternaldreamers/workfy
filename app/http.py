from flask import Flask
from flask_cors import CORS
from app.config import vars
from .endpoints import IndexView, ImagesView, WebhookView

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/images/<filename>', view_func=ImagesView.as_view('images'))
app.add_url_rule('/webhook', view_func=WebhookView.as_view('webhook'))

def setup():
    app.run(host='0.0.0.0', port=vars.HTTP_PORT)