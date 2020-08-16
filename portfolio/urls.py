from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home' ),
    path('about', views.about, name='about' ),
    path('skills', views.skills, name='skills' ),
    path('projects', views.projects, name='projects' ),
    path('anime', views.anime, name='anime' ),
    path('contact', views.contact, name='contact' ),
    
  
]