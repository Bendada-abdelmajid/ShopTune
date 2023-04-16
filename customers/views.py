

from django.shortcuts import render  ,redirect
from shopkeeper.models import Profile

from .models import Customer
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm



from django.contrib.auth import authenticate,login, logout

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail
import math, random
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from shopkeeper.models import pruduct, Review
from django.contrib import messages
from basket.models import Ordedr
from django.http import HttpResponse

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(email, name, code):
    try:
        profile=Profile.objects.all()[0]
        subject="Activate your shopytune account"
        html_content = render_to_string('registration/confirmation.html', {'name':name,'code':code, "profile": profile})
        text_content = strip_tags(html_content) 
        msg = EmailMultiAlternatives(subject, text_content,profile.email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
       return HttpResponse("somting wrong")

   
def sing_up_uesr(request):
    session_code = request.session
    massage=""
    m_type='success'
    
    if request.method == "POST":
        
        done=request.POST.get('done')
        email=request.POST.get('email')
        
        try :
            user_tesy=User.objects.get(email=email)
            massage="This email has already been registered. <br/>Please check"
            m_type='error'
        except:
            if done=='no':
                request.session['V_code'] = generateOTP()
                code = session_code.get('V_code')
                email=request.POST.get('email')
                full_name=request.POST.get('full_name')
                send_otp(email, full_name, code)
                print(code)
                massage="Verification code has been sent to your email."
                m_type='success'
            else:
                code = session_code.get('V_code')
                v_code=request.POST.get('vCode')
            
                if v_code== code:
        
                    full_name=request.POST.get('full_name')
                    email=request.POST.get('email')
                    password=request.POST.get('password')
                    phone=request.POST.get('userphone')
                    userid=list(User.objects.all())[-1].id + 1
                    
                    username='user'+str(userid)
                
                    user=User.objects.create(email=email, username=username)
                    
                    user.set_password(password)
                    user.save()
                    authenticate(username=username, password=password)
                    Customer.objects.create(user=user,full_name=full_name, Customer_phone=phone)
                    login(request, user) 
                    massage="You have been registered successfully."
                    m_type='success'
                else:
                    massage="Please enter the correct code."
                    m_type='error'
    data = {
        'message':massage,
        'type': m_type
    }

    return JsonResponse(data, safe=False)  
def login_uesr(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            username= User.objects.get(email=email).username
            user=authenticate(request, username=username ,password=password,)
            login(request, user)
            massage="ligin width success"
            m_type='success'
        except:
            if User.objects.filter(email=email).exists():
                massage="The password is incorrect, please verify"
            else :
                massage="The email is incorrect, please check." 
                 
            m_type='error'
        
    
    data = {
        'message':massage,
        'type': m_type
    }
    return JsonResponse(data, safe=False)  

def update_Profile(request, pk):
    if request.method == "POST":
        try:
            Cus=User.objects.get(pk=pk)
        
            Cus.email= request.POST.get('cus_email')
         
            Cus.customer.Customer_phone= request.POST.get("Customer_phone")
            
            Cus.customer.full_name= request.POST.get('cus_full_name')
           
            Cus.customer.save()
            Cus.save()
            
            messages.success(request, " Profile has updated with success")
        except:
            messages.error("Your account has not been modified. Please enter the correct information.")
   
    return render(request, 'registration/profile.html')
def ordersView(request):
    if request.user:
        orders= Ordedr.objects.filter(customer= request.user)
        return render(request, 'registration/orders.html', {"orders":orders})
    else :
        redirect('home')
    
def savedsView(request):
    return render(request, 'registration/saved.html')
   


  
@login_required
def changeCustomerPassword(request):
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == "POST":
        if form.errors :
            for field in form :
                for error in field.errors:
                    messages.error(request,error)
        elif form.is_valid():
            user = form.save()
            messages.success(request, "Password has updated with success")
            update_session_auth_hash(request, user)  # Important!
    return render(request, 'registration/change_password.html', {"form":form,})
def logout_user(request):
    logout(request)
    return redirect('home')


def saveProduct(request,cust, pk):
    customer = Customer.objects.get(id=cust)
    prod = pruduct.objects.get(id=pk)
    saved=False
    if prod in customer.saved.all():
        customer.saved.remove(prod)
        saved=False
    else :
        customer.saved.add(prod)
        saved=True
    customer.save()
    return JsonResponse({"saved":saved },safe=False)

def addReview(request,pk):
    data={}
    try:
        prod = pruduct.objects.get(id=pk)
        t= request.POST.get('title')
        r= request.POST.get('rate')
        content= request.POST.get('content')
        print(t)
        print(content)
        
        new_review=Review.objects.create(customer=request.user,title=t,rate=r, content=content)
        print(new_review)
        prod.riviews.add(new_review)
        new_review.save()
        data["type"]="success"
        data["message"]="review added with success"
    except:
        data["type"]="error"
        data["message"]="There is a problem, please try again."
    return JsonResponse(data,safe=False)