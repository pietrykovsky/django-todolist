from django.urls import path
from .views import about, contact, HomeView, TaskEditView, TaskDeleteView, TaskDetailView, LoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('', HomeView.as_view(), name='home'),
    path('edit/<int:pk>/', TaskEditView.as_view(), name='task-edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
    ]