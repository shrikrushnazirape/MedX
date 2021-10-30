from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def signin(request):
    return render(request, 'login.html')

def signupd(request):
    return render(request, 'doctor_signup.html')
    
def signupp(request):
    return render(request, 'patient_signup.html')

def doctord(request):
    return render(request, 'doctor_dashboard.html')

def patientd(request):
    return render(request, 'patient_dashboard.html')
