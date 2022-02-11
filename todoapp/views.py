from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm

# Create your views here.

# main view with post and get methods
# on post sending data of task to database
# on get rendering home template
class HomeView(LoginRequiredMixin, View):
    template_name = 'todoapp/home.html'
    http_methods_names = ['get', 'post']

    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.filter(user=request.user)
        paginator = Paginator(tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'form': form, 'tasks': page_obj}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

        return redirect(reverse('home'))


class TaskDetailView(LoginRequiredMixin ,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task-detail.html'


class TaskEditView(LoginRequiredMixin ,UpdateView):
    model = Task
    fields = ['title', 'is_complete']
    context_object_name = 'form'
    template_name = 'todoapp/task-edit.html'
    success_url = reverse_lazy('home')


class TaskDeleteView(LoginRequiredMixin ,DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    # overiding get method not to confirming deletion of task
    def get(self, request):
        return self.post(request)


class LoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterView(FormView):
    template_name = 'todoapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
