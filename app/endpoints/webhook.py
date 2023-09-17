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

        events = data.get('events', [])

        if events:
            current_event = events[0]
            action = current_event['action']
            resource = current_event['resource']
            gid = resource['gid']

            res = requests.get(f'https://app.asana.com/api/1.0/tasks/{gid}', headers={ 'Authorization': f'Bearer {ASANA_TOKEN}' })
            res_data = res.json().get('data', {})

            print("Query Tasks!!!")
            print(res_data)

            points_value = None
            for field in res_data.get('custom_fields', []):
                if field.get('name') == 'Points':
                    points_value = field.get('number_value')
                    break

            payload = {
                "logo": f"{request.url_root}images/asana.png",
                "assignee": res_data.get('assignee') and res_data.get('assignee').get('name'),
                "action": action,
                "due_at": res_data.get("due_at"),
                "due_on": res_data.get("due_on"),
                "name": res_data.get("name"),
                "notes": res_data.get("notes"),
                "points": points_value
            }

            print("Send Payload!!!")
            print(payload)

            emitter.emit(EVENT_WEBHOOK, payload)

        response = Response(EMTY_RESPONSE, status=200)
        response.headers["X-Hook-Secret"] = hook_secret

        return response
