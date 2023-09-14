from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('landing', views.landing, name='landing'),
   path('', views.home_load, name='home'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
     path('pricing', views.pricing, name='pricing'),
      
 #    path('upload/', views.upload_document, name='upload_document'),
]