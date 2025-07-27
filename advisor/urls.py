from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diagnosis/<str:animal_type>/', views.diagnosis, name='diagnosis'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('contact/',views.contact, name='contact'),
]
