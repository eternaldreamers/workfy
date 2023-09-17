import os
from PIL import Image
from flask import send_from_directory
from flask.views import MethodView

class ImagesView(MethodView):
    def get(self, filename: str):
        folder_path = os.path.join(os.getcwd(), "static/images")
        # image_path = f"{folder_path}/{filename}"
        # img = Image.open(image_path)
        return send_from_directory(folder_path, filename)