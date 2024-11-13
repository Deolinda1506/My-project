from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def call(request):
    return render(request, 'teleconsultation/call.html')
