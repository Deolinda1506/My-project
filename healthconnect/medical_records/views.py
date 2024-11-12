from django.shortcuts import render, redirect
from .models import MedicalRecord
from django.contrib.auth.decorators import login_required

@login_required
def view_records(request):
    records = MedicalRecord.objects.filter(patient=request.user) if request.user.role == 'patient' else MedicalRecord.objects.filter(doctor=request.user)
    return render(request, 'medical_records/view.html', {'records': records})

@login_required
def add_record(request):
    if request.method == 'POST' and request.user.role == 'doctor':
        record = MedicalRecord(
            patient=User.objects.get(id=request.POST['patient_id']),
            doctor=request.user,
            diagnosis=request.POST['diagnosis'],
            prescription=request.POST['prescription']
        )
        record.save()
        return redirect('view_records')
    patients = User.objects.filter(role='patient')
    return render(request, 'medical_records/add.html', {'patients': patients})

