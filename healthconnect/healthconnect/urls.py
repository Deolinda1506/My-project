from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple home view
def home(request):
    return HttpResponse("<h1>Welcome to HealthConnect</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page URL
    path('auth/', include('authentication.urls')),  # Include URLs for authentication app
    path('appointments/', include('appointments.urls')),  # Include URLs for appointments app
    path('medical_records/', include('medical_records.urls')),  # Include URLs for medical records app
    path('teleconsultation/', include('teleconsultation.urls')),  # Include URLs for teleconsultation app
]
