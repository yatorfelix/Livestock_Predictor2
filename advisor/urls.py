from django.urls import path
from . import views
from .views import medication_calculator


urlpatterns = [
    path('', views.home, name='home'),
    path('diagnosis/<str:animal_type>/', views.diagnosis, name='diagnosis'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('contact/',views.contact, name='contact'),
    path('diagnose/<str:animal_type>/', views.diagnosis, name='diagnosis'),
    path('diagnose/<str:animal_type>/report/', views.diagnosis_report, name='diagnosis_report'),
    path('calculator/', medication_calculator, name='medication_calculator'),
    path('weather-advice/', views.weather_advice, name='weather_advice'),

]
