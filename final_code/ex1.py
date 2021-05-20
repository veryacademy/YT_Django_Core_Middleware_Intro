# Basic framework

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


class ExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        

    def __call__(self, request):
        # Logic executed on a request before the view (and other middleware) is called.
        # get_response call triggers next phase
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.
        # Return response to finish middleware sequence
        return response