class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # https://docs.djangoproject.com/en/3.2/ref/request-response/
        print(request.path)
        print(request.headers['Host'])
        print(request.headers['Accept-Language'])
        print(request.META['REQUEST_METHOD'])
        print(request.META['HTTP_USER_AGENT'])

        # https://github.com/selwin/django-user_agents
        # print(request.user_agent.is_pc)

        response = self.get_response(request)

        return response
    