from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserForm, TaskForm
from django.views.generic import ListView
from .models import Task
from django.urls import reverse_lazy


# Create your views here.
def about(request):
    template = loader.get_template('todoapp/about.html')
    return HttpResponse(template.render({},request))

def contact(request):
    template = loader.get_template('todoapp/contact.html')
    return HttpResponse(template.render({},request))

class TaskListView(ListView):
    model = Task
    template_name = 'todoapp/home.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'todoapp/task-form.html'
    fields = ['title']
    context_obect_name = 'tasks'
    success_url = reverse_lazy('home')

class TaskEditView(UpdateView):
    model = Task
    template_name = 'todoapp/task-form.html'
    fields = ['title']
    context_obect_name = 'tasks'
    success_url = reverse_lazy('home')

class TaskDelete(DeleteView):
    pass
