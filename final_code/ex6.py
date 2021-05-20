class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.context_responce = {
            "msg": {"warning": "There is no more ink in the printer"},
        }

    def __call__(self, request):

        response = self.get_response(request)

        return response
    
    def process_template_response(self, request, response):
        response.context_data["new_data"] = self.context_responce
        return response
        