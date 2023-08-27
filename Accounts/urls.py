from django.urls import path
from .import views

urlpatterns = [
    path('',views.loginpage, name='login'),
     path('home/',views.home, name='home'),
     path('signup/',views.signup, name='signup'),
]
