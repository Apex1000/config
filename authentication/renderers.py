from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""
        if "ErrorDetail" in str(data):
            response = json.dumps({"error": "user with this email already exists."})
        else:
            response = json.dumps({"data": data})
        return response


class LoginRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""
        if "ErrorDetail" in str(data):
            response = json.dumps(
                {"error": "Invalid credentials or incorrect email address."}
            )
        else:
            response = json.dumps({"data": data})
        return response
