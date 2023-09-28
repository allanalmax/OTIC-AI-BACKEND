from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
   # path('', views.home_load, name='home'),
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
      path('landing', views.landing, name='landing'),
     path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path("message/", views.whatsappreply,name='whatsapp'),
    path('logout', views.logout, name='logout'),
      path('find/',views.FindReset,name='find'),
path('reset/done/', views.password_reset_complete, name="password_reset_complete"),
   path('password-reset/', PasswordResetView.as_view(template_name='changepassword.html'), name='password-reset'),
   path('activate/<uid64>/<token>', views.activate, name="activate"),
   
]