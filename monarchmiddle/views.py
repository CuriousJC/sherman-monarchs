# monarchmiddle/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

def password_protect(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == settings.PASSWORD_PROTECT:
            request.session['authenticated'] = True
            return redirect(request.GET.get('next', '/'))
        else:
            return HttpResponse("Incorrect password. Please try again.")

    return render(request, 'monarchmiddle/password_protect.html')

