from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('signupp/',views.signupp, name='patient_signup'),
    path('doctor/', views.doctord, name='ddash'),
    path('patient/', views.patientd, name='pdash'),
    path('new/', views.new, name='new'),
    path('getp/', views.getp, name='getp')
]
