class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exceptions = 0

    def __call__(self, request):

        response = self.get_response(request)

        return response
    
    def process_exception(self, request, exception):
        self.num_exceptions += 1
        print(f"Expection count:{self.num_exceptions}")

    # def process_template_response(self, request, response):
    #     pass


