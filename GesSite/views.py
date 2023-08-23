from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Portfolio



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def teams(request):
    return render(request, 'teams.html')

def portfolio(request):
    photo = Portfolio.objects.all()
    return render(request, 'Portfolio.html')

def blog(request):
    return render(request, 'blog.html')


# Create your views here.
