from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to HealthConnect</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('auth/', include('authentication.urls')),  # Authentication URLs
    path('appointments/', include('appointments.urls')),  # Appointments URLs
    path('medical_records/', include('medical_records.urls')),  # Medical records URLs
    path('teleconsultation/', include('teleconsultation.urls')),  # Teleconsultation URLs
]
