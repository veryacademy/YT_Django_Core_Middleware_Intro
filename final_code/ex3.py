class ExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view
        # Gives access to the view itself & arguments
        pass

    def process_exception(self,request, exception):
        # Logic executed if an exception/error occurs in the view
        pass

    def process_template_response(self,request, response):
        # Logic executed after the view is called, 
        # ONLY IF view response is TemplateResponse, see listing 2-24 
        pass