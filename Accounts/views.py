from django.shortcuts import render

# Create your views here.
def loginpage (request):
    return render(request,'login.html')

def signup (request):
    return render(request,'signup.html')

def home (request):
    return render(request,'home.html')