class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.num_requests = 0

    def __call__(self, request):

        self.num_requests += 1
        print(f"Requests handled so far: {self.num_requests}")

        response = self.get_response(request)

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'View Name: {view_func.__name__}')
        return None

    # def process_exception(self,request, exception):
    #     pass

    # def process_template_response(self,request, response):
    #     pass
