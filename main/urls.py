# general imports
from django import views
from django.urls import path
from main import views

# general urls
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]
