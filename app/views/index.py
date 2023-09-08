from flask.views import MethodView

class IndexView(MethodView):
    def get(self):
        return "Hello World"