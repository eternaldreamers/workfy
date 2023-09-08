from flask.views import MethodView
from app.config.events import emitter
from app.config.constants import EVENT_WEBHOOK, EMTY_RESPONSE

class WebhookView(MethodView):
    def post(self):
        emitter.emit(EVENT_WEBHOOK, 'send messagexxxxx!')
        return EMTY_RESPONSE, 200