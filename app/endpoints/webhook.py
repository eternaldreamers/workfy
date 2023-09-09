import requests
from flask.views import MethodView
from flask import request, Response
from app.config.events import emitter
from app.config.vars import ASANA_TOKEN
from app.config.constants import EVENT_WEBHOOK, EMTY_RESPONSE

class WebhookView(MethodView):
    def post(self):
        hook_secret = request.headers.get('X-Hook-Secret')
        data = request.get_json()

        print("Listen Webhook!!!")
        print(data)

        events = data['events']

        if len(events):
            current_event = events[0]
            resource = current_event['resource']
            gid = resource['gid']

            res = requests.get(f'https://app.asana.com/api/1.0/tasks/{gid}', headers={ 'Authorization': f'Bearer {ASANA_TOKEN}' })
            res_data = res.json()

            print("Query Tasks!!!")
            print(res_data)

            payload = {
                "due_at": res_data["due_at"],
                "due_on": res_data["due_on"],
                "name": res_data["name"],
                "notes": res_data["notes"]
            }

            emitter.emit(EVENT_WEBHOOK, payload)

        response = Response(EMTY_RESPONSE, status=200)
        response.headers["X-Hook-Secret"] = hook_secret

        return response



