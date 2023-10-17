from django.http import HttpResponse
from django.shortcuts import render
from .models import Monarch

def monarchs(request):
    monarchs_data = Monarch.objects.all()
    return render(request,"monarchs/monarchs.html", {'monarchs_data' : monarchs_data})

def home(request):
    return HttpResponse("Home Page")

def monarch_detail(request, id):
    monarch_detail = Monarch.objects.get(pk=id)
    return render(request, "monarchs/monarch_detail.html", {'monarch': monarch_detail})