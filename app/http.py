from flask import Flask
from app.config import vars
from .views import IndexView, WebhookView

app = Flask(__name__)

app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/webhook', view_func=WebhookView.as_view('webhook'))

async def setup():
    app.run(host='0.0.0.0', port=vars.HTTP_PORT)