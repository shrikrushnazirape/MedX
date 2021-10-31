from django.http.response import FileResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.urls.resolvers import LocalePrefixPattern
from .models import Doctor , Patient, Prescription, Medecine

# Create your views here.
def signin(request):
    login_page_path = 'login2.html'

    if request.user.is_authenticated:
        print("test1")
        if(request.user.is_staff):
            return redirect("ddash")
        else:
            return redirect("pdash")

    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            if (user.is_staff):

                auth.login(request, user)
            
                return redirect("ddash")
            else:
                
                patient = Patient.objects.get(user = user)
                auth.login(request, user)
                return redirect("pdash")
        return render(request, login_page_path, {'msg': 'Invalid Credentials!'})
    return render(request, login_page_path)
   

def signupd(request):
    register_doctor = 'doctor_signup.html'
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('login')
        data = request.POST
        username = data['username']
        password = data['password']
        password2 = data['password2']
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        phone = data['phone']
        address = data['add']
        clinic_name = data['cname']
        ddetail = data['ddetail']
        edeatil = data['ed']

        if password != password2:
            return render(request, register_doctor, {'msg': ["Passwords Don't match"]})
      
        if len(password) == 0:
            return render(request, register_doctor, {'msg': ["Please enter password"]})

        try:
            user1 = User.objects.create(username = username, first_name = fname, last_name = lname, email = email, password = password)
            Doctor.objects.create(
                user = user1,
                edu_details = edeatil,
                doc_details = ddetail,
                Address = address,
                contact = phone,
                clinic_name = clinic_name,

                )
            user1.is_staff = True
            user1.save()
            auth.login(request, user1)
            return redirect('ddash')
        except Exception as e:
            return render(request, register_doctor, {'msg': [f'User already exists..!!{e}']})
            
    return render(request, register_doctor)
  
    
def signupp(request):
    register_patient = 'patient_signup.html'
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('login')
        data = request.POST
        username = data['username']
        password = data['password']
        password2 = data['password2']
        fname = data['fname']
        lname = data['lname']
        email = data['email']

        dob = data['dob']
        height = data['height']
        weight = data['weight']
        bloodgroup = data['bloodgroup']
        contact = data['contact']
        pre_hist = data['pre_hist']

        if password != password2:
            return render(request, register_patient, {'msg': ["Passwords Don't match"]})
      
        if len(password) == 0:
            return render(request, register_patient, {'msg': ["Please enter password"]})

        try:
            user1 = User.objects.create(username = username, first_name = fname, last_name = lname, email = email, password = password)
            Patient.objects.create(
                user = user1,
                dob = dob,
                height = height,
                weight = weight,
                bloodgroup = bloodgroup,
                contact = contact,
                pre_med_hist = pre_hist
                )
            user1.save()
            auth.login(request, user1)
            return redirect('pdash')
        except Exception as e:
            return render(request, register_patient, {'msg': [f'User already exists..!!{e}']})
  
    return render(request, register_patient)
  

def doctord(request):
    ddash = 'doctor_dashboard.html'
    if request.user.is_authenticated and request.user.is_staff:
        d_obj = Doctor.objects.get(user = request.user)
        pre_obj = Prescription.objects.filter(doctor_id = d_obj)
        t_data= {}
        for item in pre_obj:
            meditem = Medecine.objects.filter(prescription = item)      
            t_data[item] = meditem
        data = {
            'd_obj':d_obj,
            'pre_obj':pre_obj,
            't_data':t_data
         
        }
        return render(request, ddash, data)

    return redirect('login')
   

def patientd(request):
    
    pdash = 'patient_dashboard.html'
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      
        p_obj = Patient.objects.get(user = request.user)
      
        pre_obj = Prescription.objects.filter(patient_id = p_obj)
        
        t_data= {}
        for item in pre_obj:
            meditem = Medecine.objects.filter(prescription = item)      
            t_data[item] = meditem
               
        
        data = {
            'p_obj':p_obj,
            'pre_obj':pre_obj,
            't_data':t_data
         
        }
        for item in t_data:
            print (t_data[item])

        return render(request, pdash, data)
    print("Not authen")
    return redirect('login')
   
def signout(request):
    try:
        logout(request)
        return redirect('login')
    except:
       return HttpResponse("Need to Login First")


def new(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'new_presc.html')
    return redirect('login')

import json
def entry(request):
    if request.user.is_authenticated and request.user.is_staff:
        if(request.method == 'POST'):
            data = request.POST
          
            temp = (data['datamain'])
            pid = data['patient']

            
            try:
                p_obj = Patient.objects.get(patient_id = pid)
                d_obj = Doctor.objects.get(user = request.user)
                presc_obj = Prescription.objects.create(doctor_id=d_obj, patient_id = p_obj)
                presc_obj.save()
                json_obj = json.loads(temp)
                for item in json_obj:
                    med_it = Medecine.objects.create(prescription = presc_obj, med_name = item['med'], qty= item['qty'], dose=item['dose'])
                    med_it.save()
                return JsonResponse({"success": "Successfully Saved"},status=200)

            except Exception as e:
           
                
                return JsonResponse({"success": "Not Found Enter Correct Details"},status=200)
            # pid = (data['patient'])
            # print("PID is : ", pid)
            
            return JsonResponse({"success": "Milestone successfully created"},status=200)
        return JsonResponse({"error": "Invalid Path"},status=403)  
    return JsonResponse({"error": "Login to the system"},status=403)


def pharma(request):
    temp = 'pharma_dash.html'
    if(request.method == 'POST'):
        data = request.POST
        pid = (data['pid'])
        psid = data['psid']

        try:
            # return JsonResponse({"success": "Not Found Enter Correct Details"},status=200)
            p_obj = Patient.objects.get(patient_id=pid)
            ps_obj = Prescription.objects.get(pk = psid)
           
            if(ps_obj.patient_id == p_obj):
                meditem = Medecine.objects.filter(prescription = ps_obj)
                data = {
                    'meditem':meditem,
                    'p_obj':p_obj
                }
                
                return render(request, 'pharmalist.html', data)
            else:
                return render(request, temp, {'msg': "incorrect Details"})
        except Exception as e:
            print(e)
            return render(request, temp, {'msg': "incorrect Details"})
    return render(request, 'pharma_dash.html')



def getPresc(request):

    return render(request, 'pharmalist.html')