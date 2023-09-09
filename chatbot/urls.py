from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
   # path('', views.home_load, name='home'),
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
     path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
      
 #    path('upload/', views.upload_document, name='upload_document'),
]