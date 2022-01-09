from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from django.views.generic import ListView
from .models import Task

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

class TaskListView(ListView):
    model = Task
    template_name = 'todoapp/home.html'
    context_object_name = 'task'

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'todoapp/login'

#     def get(self, request):
#         form = self.form_class(None)
#         context = {'form': form}
#         return render(request, self.template_name, context)

#     def post(self, request):
#         pass