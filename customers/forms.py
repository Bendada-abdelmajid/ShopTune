from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

# class editProfile_Form(UserChangeForm):
class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'required':True}),)
    Customer_phone=forms.IntegerField(widget=forms.NumberInput(attrs={'required':True}),)
    class Meta:
        model=User
        fields=('username','email', 'password1',)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
       
        self.fields['username'].label = "الاسم الكامل"
        
        self.fields['email'].label = "البريد الإلكتروني"
      
        self.fields['password1'].label ='كلمة السر'
       
    

       
        self.fields['Customer_phone'].label = "هاتف"
        
class editUserForm(UserChangeForm):
    Customer_phone=forms.IntegerField(widget=forms.NumberInput(attrs={'required':True}),)
    full_name=forms.CharField(max_length=50, widget=forms.TextInput())
    email=forms.EmailField(widget=forms.EmailInput())
    class Meta:
        model=User
        fields=('full_name','email','Customer_phone')