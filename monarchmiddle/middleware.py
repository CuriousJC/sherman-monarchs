from django.http import HttpResponseRedirect
from django.conf import settings

class PasswordProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.password = settings.PASSWORD_PROTECT
        self.password_protect_url = '/password_protect/'  # Adjust this to your actual password protection URL

    def __call__(self, request):
        if request.path_info != self.password_protect_url and not request.session.get('authenticated', False):
            # User is not authenticated and not accessing the password protection URL, redirect to password page
            return HttpResponseRedirect(self.password_protect_url)

        response = self.get_response(request)
        return response
