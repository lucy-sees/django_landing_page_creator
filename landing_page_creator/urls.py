from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-app/', views.create_app, name='create_app'),
]