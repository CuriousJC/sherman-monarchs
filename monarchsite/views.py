from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Monarch

def monarchs(request):
    monarchs_data = Monarch.objects.all()
    return render(request,"monarchs/monarchs.html", {'monarchs_data' : monarchs_data})

def home(request):
    return HttpResponse("Home Page")

def monarch_detail(request, id):
    monarch = Monarch.objects.get(pk=id)
    return render(request, "monarchs/monarch_detail.html", {'monarch': monarch})

def monarch_add(request):
    monarch_name = request.POST.get('name')
    monarch_path = request.POST.get('path')
    monarch_aspects = request.POST.get('aspect')

    # when things got populated via the POST we would go ahead and save this new model to the db
    if monarch_name and monarch_path and monarch_aspects:
        monarch = Monarch(name=monarch_name, path=monarch_path, aspect=monarch_aspects)
        monarch.save()
        return HttpResponseRedirect('/monarchs')

    return render(request, "monarchs/monarch_add.html")

def monarch_delete(request, id):
    try:
        monarch = Monarch.objects.get(pk=id)
    except:
        raise Http404('Monarch does not exist')
    
    monarch.delete()
    return HttpResponseRedirect('/monarchs')