from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('', views.TaskListView.as_view(), name='home'),
    path('create-task/', views.TaskCreateView.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', views.TaskEditView.as_view(), name='edit-task')
    ]