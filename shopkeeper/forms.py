

from django import forms
from .models import pruduct, categorys, Profile, mainCat, subCat, Color
from colorfield.fields import ColorField
class PruductForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
            })
    )
    class Meta:
        model = pruduct
        fields = ['title','category','price','discount', 'description', 'colors', 'size', 'size2', 'size3', 'size4']
        widgets= {
          'description': forms.Textarea(attrs={'placeholder':'add description'}), 
          'title': forms.TextInput(attrs={'placeholder':'add title'}), 
          'price': forms.NumberInput(attrs={'placeholder':'add price'}), 
          'discount': forms.NumberInput(attrs={'placeholder':'add discount'}), 
          'colors':forms.SelectMultiple(attrs={'placeholder':'select colors'}),
          'size': forms.TextInput(attrs={'placeholder':'add size','class':'size'}), 
          'size2': forms.TextInput(attrs={'placeholder':'add size' ,'class':'size'}), 
          'size3': forms.TextInput(attrs={'placeholder':'add size', 'class':'size'}), 
          'size4': forms.TextInput(attrs={'placeholder':'add size', 'class':'size'}), 
        }
       
class MainCatForm(forms.ModelForm):
    class Meta:
        model =mainCat 
        fields = ['name']
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hex_color']
        widgets= {
            'hex_color': forms.TextInput(attrs={'type':'color'}),  
        }
class SubCatForm(forms.ModelForm):
    class Meta:
        model = subCat
        fields = ['main_cat','name']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = categorys
        
        fields = ['main_cat', "sub_cat",'name']

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('address','phone','facebook','instagram', 'tiktok')
        widgets= {
          'email_password': forms.PasswordInput(),}
       
       
       
    