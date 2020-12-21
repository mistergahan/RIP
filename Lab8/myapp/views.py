from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Detail

def master(request):
    template = loader.get_template("master.html")
    context = {
            "details": Detail.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    template = loader.get_template("detail.html")
    context = {
            "detail": Detail.objects.get(id=id),
    }
    return HttpResponse(template.render(context, request))
