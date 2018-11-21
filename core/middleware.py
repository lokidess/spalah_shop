import datetime

from django.utils.deprecation import MiddlewareMixin


class TimeOfView(MiddlewareMixin):

    time = None

    def process_request(self, request):
        # print(dir(request))
        print(request.META['HTTP_HOST'])
        protocol = 'https' if request.is_secure() else "http"
        self.time = datetime.datetime.now()

    def process_response(self, request, response):
        print((datetime.datetime.now() - self.time).microseconds)
        return response
