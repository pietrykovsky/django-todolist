from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('todoapp/home.html')
    return HttpResponse(template.render({},request))

def about(request):
    template = loader.get_template('todoapp/about.html')
    return HttpResponse(template.render({},request))

def contact(request):
    template = loader.get_template('todoapp/contact.html')
    return HttpResponse(template.render({},request))