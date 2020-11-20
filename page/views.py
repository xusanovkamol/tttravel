from django.shortcuts import render
from django.http import HttpResponse
from .models import destinations
# Create your views here.

def home(request):
    dests= destinations.objects.all()

    return render(request, 'index.html',{'dests':dests})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def manzil(request):
    return render(request, 'destinations.html')

def elements(request):
    return render(request, 'elements.html')

def news(request):
    return render(request, 'news.html')
