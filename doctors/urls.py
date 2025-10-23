from django.urls import path
from . import views

app_name = 'doctors'  # Namespace for URL names to avoid conflicts

urlpatterns = [
    path('', views.home, name='home'),  # Home page at root of app
    path('doctors/', views.doctors_list, name='doctors_list'),  # List of doctors with search
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),  # Detail view for a specific doctor
    path('about/', views.about, name='about'),  # About page
]
