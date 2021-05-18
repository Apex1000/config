import json

from rest_framework.renderers import JSONRenderer


class CoreJSONRenderer(JSONRenderer):
    charset = "utf-8"
    object_label = "object"

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        errors = data.get("errors", None)

        if errors is not None:
            # As mentioned about, we will let the default JSONRenderer handle
            # rendering errors.
            return super(CoreJSONRenderer, self).render(data)

        return json.dumps({self.object_label: data})


class DemoRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""
        if "ErrorDetail" in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps(
                {
                    "status": True,
                    "result": data,
                    "message": "User Login",
                    "statusCode": 200,
                }
            )
        return response


class DataRenderer(JSONRenderer):
    charset = "utf-8"
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""
        if "ErrorDetail" in str(data):
            response = json.dumps({"error": "data"})
        else:
            return json.dumps( {
                "total_count":data['count'],
                "incomplete_results":False,
                "items":data['results']
            })
        return response
