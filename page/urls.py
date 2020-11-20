from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('destinations.html', views.manzil, name='destinations'),
    path('elements.html', views.elements, name='elements'),
    path('news.html', views.news, name='news'),
]