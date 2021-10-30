from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def signin(request):
    return HttpResponse("Login page")

def signupd(request):
    return HttpResponse("doctor signup page")
    

def signupp(request):
    return HttpResponse("patient signup page")

def doctord(request):
    return HttpResponse("doctor dashbaord")

def patientd(request):
    return HttpResponse("patient dashbaord")
