from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactFormView, ContactResultView

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home' ),
    path('about', views.about, name='about' ),
    path('skills', views.skills, name='skills' ),
    path('projects', views.projects, name='projects' ),
    path('anime', views.anime, name='anime' ),
    # path('contact', views.contact, name='contact' ),
    
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
]