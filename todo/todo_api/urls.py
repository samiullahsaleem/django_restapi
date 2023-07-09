from django.urls import path, include
from todo_api import views

urlpatterns = [
    path('api', views.get),
]