from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('', views.TaskListView.as_view(), name='home')
    ]