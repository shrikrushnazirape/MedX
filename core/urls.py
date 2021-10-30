from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.signin, name='login'),
    path('signupd/',views.signupd, name='docter_signup'),
    path('signupp/',views.signupp, name='patient_signup'),
    path('doctor/', views.doctord, name='doctor_dashboard'),
    path('patient/', views.patientd, name='pateint_dashboard'),
]
