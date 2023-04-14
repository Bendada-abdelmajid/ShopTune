

# from ossaudiodev import SOUND_MIXER_MONITOR
# from typing_extensions import Self
from django.shortcuts import render, redirect
from .models import pruduct, Image, categorys, Profile, TodoList, subCat, mainCat, Color
from basket.models import Ordedr
from django.core import serializers

from django.http import JsonResponse
from .forms import PruductForm, CategoryForm, ProfileForm, SubCatForm, MainCatForm, ColorForm

import os
from cloudinary.forms import cl_init_js_callbacks
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.files.storage import FileSystemStorage
from calendar import HTMLCalendar
from django.contrib.auth import logout
from datetime import datetime, date, timedelta
from store.views import pagination
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def adminPage(request):
    month=datetime.now().month
    year=datetime.now().year
    day = datetime.now().day
 
    if request.POST.get('direction'):
        month= int(request.POST.get('mun'))
        year= int(request.POST.get('year'))
        data = {
            'cal':HTMLCalendar().formatmonth(year, month),
        }
        return JsonResponse(data, safe=False)
    cal=HTMLCalendar().formatmonth(year, month)
    orders=Ordedr.objects.filter(complet=False)
    products=pruduct.objects.filter(out_of_stock=True)  
    todos=TodoList.objects.all().order_by('todo_date')
    for todo in todos:
        if todo.todo_date.year <= year and todo.todo_date.month <= month and  todo.todo_date.day < day:
            todo.delete()
    return render(request, 'admin_pages/dashboard.html', {'orders':orders,'products':products, 'cal':cal, 'month':month, 'year': year, 'todos': todos,})
def order_detail(request, pk):
    order=Ordedr.objects.get(pk= pk)
    order.has_seen=True
    order.save()
    return render(request, 'admin_pages/order_detail.html', {'order':order})

def addTodo(request):
    todo= request.POST.get('todo')
    date= request.POST.get('date')
    newTodo=TodoList.objects.create(todo=todo, todo_date=date)
    data= {
        'todo':todo,
        'date':date,
        'id':newTodo.id,
    }

    print(data)
    return JsonResponse(data,safe=False)
def deleteTodo(request, pk):
    todo= TodoList.objects.get(pk=pk)
    data= {}
   
    todo.delete()
    return JsonResponse(data,safe=False)
def order_hasSeen(request, pk):
    order=Ordedr.objects.get(pk= pk)
    order.has_seen=True
    data= {
        'has_seen':True
    }
    order.save()
    return JsonResponse(data,safe=False)
def order_hascomplet(request, pk):
    order=Ordedr.objects.get(pk= pk)
    order.complet=True
    data= {
        'complet':True
    }
    order.save()
    if request.method == "POST":
        return JsonResponse(data,safe=False)
    else:
        return render(request, 'admin_pages/order_detail.html', {'order':order})
def delete_order(request, pk):
    order=Ordedr.objects.get(pk= pk)
    order_name=order.customer
    order.delete()
    messages.success(request, f" {order_name} Has been deleted successfully")
    return redirect('orders')
 
def AddPruduct(request):
   
    form = PruductForm(request.POST, request.FILES)
    files = request.FILES.getlist('image')
    if form.errors :
        for field in form :
            for error in field.errors:
                print(error)
    if form.is_valid():
        prud = form.save(commit=False)
        prud.save()
        for f in files:
            img = Image(image=f)
            img.save()
            prud.image.add(img)
        prud.colors.set(request.POST.getlist('colors'))
        prud.chanegePrice()
        prud.save()
        messages.success(request, "Has been added with success.")
        return redirect('add-pruduct')
   

    return render(request, 'admin_pages/add/add_pruduct.html', {'form': form})
def AddMainCategory(request):
    form = MainCatForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Has been added with success.")
        return redirect('add-main-category')
    
    return render(request, 'admin_pages/add/add_main_cat.html', {'form': form})
def AddSubCategory(request):
    form = SubCatForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Has been added with success.")
        return redirect('add-sub-category')

    
    return render(request, 'admin_pages/add/add_sub_cat.html', {'form': form})
def AddCategory(request):
    form = CategoryForm(request.POST, request.FILES)
    cats={}
    for x in mainCat.objects.all():
        subList=[]
        for s in subCat.objects.filter(main_cat= x):
            subList.append({"name": s.name, "id": s.id})
        cats[x.id]= subList
    if form.is_valid():
        form.save()
        messages.success(request, "Has been added with success.")
        return redirect('add-category')
    return render(request, 'admin_pages/add/add_category.html', {'form': form, "sub_cats":cats})
def AddColor(request):
    form = ColorForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Has been added with success.")
        return redirect('add-color')
    
    return render(request, 'admin_pages/add/add_color.html', {'form': form})
def editProduct(request, pk):
    prod=pruduct.objects.get(pk= pk)
    form=PruductForm(request.POST or None, instance=prod)
    if form.is_valid():
        if len(request.FILES)!=0:
            files = request.FILES.getlist('image')
            if prod.image.all().count() > 0:
                for img in prod.image.all():
                    prod.image.remove(img)
                   
            for f in files:
                img = Image(image=f)
                img.save()
                prod.image.add(img)
        prod.chanegePrice()
        form.save()
        messages.success(request, "Successfully updated product width.")
        return redirect("products")
    return render(request, 'admin_pages/edit-product.html', {
        "form":form,
        "prod": prod})
def editMainCategory(request, pk):
    cat=mainCat.objects.get(pk= pk)
    form=MainCatForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        messages.success(request, "Has been updated  with success.")
        return redirect("main-category")
    return render(request, 'admin_pages/add/add_main_cat.html', {
        "form":form,"edit":True})
def editSubCategory(request, pk):
    cat=subCat.objects.get(pk= pk)
    form=SubCatForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        messages.success(request, "Has been updated  with success.")
        return redirect("sub-category")
    return render(request, 'admin_pages/add/add_sub_cat.html', {
        "form":form,"edit":True})
def editCategory(request, pk):
    cat=categorys.objects.get(pk= pk)
    form=CategoryForm(request.POST or None, instance=cat)
    cats={}
    for x in mainCat.objects.all():
        subList=[]
        for s in subCat.objects.filter(main_cat= x):
            subList.append({"name": s.name, "id": s.id})
        cats[x.id]= subList
    if form.is_valid():
        form.save()
        messages.success(request, "Has been updated  with success.")
        return redirect("categories")
    return render(request, 'admin_pages/add/add_category.html', {
        "form":form,"edit":True,"sub_cats":cats, "sub": cat.sub_cat.name})
def change_state(request, pk):
    prud=pruduct.objects.get(pk= pk)
    state=request.POST.get('state')
    if state== 'False':
        prud.out_of_stock=True
    else:
        prud.out_of_stock=False
    data= {
        'state':state
    }
    prud.save()
    return JsonResponse(data,safe=False)

def add_more_info(request, pk):

    profile= Profile.objects.get(pk=pk)
    user=request.user
    if request.method == "POST":
        if user.is_superuser:
            user.email= request.POST.get('email')
            user.customer.full_name= request.POST.get('full_name')
            profile.facebook= request.POST.get('facebook')
            profile.tiktok= request.POST.get('tiktok')
            profile.instagram= request.POST.get('instagram')
            profile.address= request.POST.get('address')
            profile.phone= request.POST.get('phone')
            profile.email= request.POST.get('email')
            user.save()
            profile.save()
            messages.success(request, "Your profile has been updated  with success.")
            return redirect("/shopkeeper/Profiel/1")
    return render(request, 'admin_pages/add_more_info.html', {})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'لقد تم تغيير كلمة المرور بنجاح')
            return redirect('change-password')
        else:
            messages.error(request, 'المرجو مراجعة الأ خطاء التالية')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin_pages/change_password.html', {'form': form })
    
    
def get_notifs(request):
    data=Ordedr.objects.filter(has_seen=False).order_by('-oreder_date')
    jsonData=serializers.serialize('json', data)
    return JsonResponse({'data':jsonData})


def order_category_summary(request, type):
    todays_date = date.today()
    prev_week_ago = todays_date-timedelta(days=7)
    prev_month_ago=todays_date-timedelta(days=30)
    if type== 'month':
        orders = Ordedr.objects.filter(oreder_date__gte=prev_month_ago)
    elif type =='week':
        orders = Ordedr.objects.filter(oreder_date__gte=prev_week_ago)
    
    finalrep = {}
    products_list = []
    for o in orders:
        for p in o.products.all():
            products_list.append(p.product.title)
 
    for x in orders:
        for y in list(set(products_list)):
            finalrep[y] = products_list.count(y)
    finalList=dict(sorted(finalrep.items(), key=lambda x: x[1], reverse=True)[:5])
    data={'order_data': finalList}
    return JsonResponse(data, safe=False)






def general_searsh(request, o):
    context={}
    search_elments=""
    print(o)
    q= request.GET.get('q')
    
    if o =="o":
        search_elments=Ordedr.objects.filter(customer__customer__full_name__icontains=q)
    elif o=="main_c":
        search_elments=mainCat.objects.filter(name__icontains=q)
    elif o=="sub_c":
        search_elments=subCat.objects.filter(name__icontains=q)
    elif o=="c":
        search_elments=categorys.objects.filter(name__icontains=q)
    elif o=="p":
        mutiple_q=Q(Q(title__icontains=q)  |Q(category__name__icontains=q) )
        search_elments=pruduct.objects.filter(mutiple_q)
   
    p=Paginator(search_elments, 1)
    page=request.GET.get('page')
    products=p.get_page(page)
    print(products)
    page_range= pagination(products)
    count=len(search_elments)
    context['page_range']=page_range
    context['qwery']=products
    context['count']=count
    context['q']=q
    return context

def general_view(request, obj, o, url):
    context={}
    if request.GET.get('q'):
        context=general_searsh(request, o)
    elif request.GET.get('select'):
        select= request.GET.get('select')
        print(select)
        if select == 'All':
            context['qwery']=obj.objects.all()
        else:
            print(select)
            if obj == pruduct:
                context['qwery']=pruduct.objects.filter(out_of_stock=select)
            elif obj == Ordedr:
                context['qwery']=Ordedr.objects.filter(complet=select)
        context['select']=select
    else:
        orders=obj.objects.all()
        context['qwery']=orders
    if request.method == "POST":
        print('yes')
        orders_ids=request.POST.getlist('id[]')
        for id in orders_ids:
            order= obj.objects.get(pk=id)
            order.delete()
        return redirect(url)
    return render(request, f"admin_pages/{url}.html", context)
def allOreders_view(request):
    return   general_view(request,Ordedr, 'o', 'orders')
def Product_view(request):
    return   general_view(request,pruduct, 'p', 'products')

 
def main_categories_view(request):
    context={}
    if request.GET.get('q'):
        context=general_searsh(request, 'main_c') 
    else:
        data=mainCat.objects.all()
        context['qwery']=data
    if request.method == "POST":
        delte(request, mainCat)  
    context['qwery']=map(lambda x: {"id":x.id,'link': "/shopkeeper/categories/"+ x.slug, "name": x.name,"edit":f"/shopkeeper/edit-main-category/{x.id}"}, context['qwery'] )
    return render(request, f"admin_pages/category.html", context)
def sub_categories_view(request,main):
    context={}
    if request.GET.get('q'):
        context=general_searsh(request, 'sub_c') 
    else:
        data=subCat.objects.filter(main_cat__slug= main)
        context['qwery']=data
    if request.method == "POST":
        delte(request, subCat)  
    context['main']=main.replace("-", " ")
    context['qwery']=map(lambda x: {"id":x.id,'link': f"/shopkeeper/categories/{main}/{x.slug}", "name": x.name, "edit":f"/shopkeeper/edit-sub-category/{x.id}" }, context['qwery'] )
    return render(request, f"admin_pages/category.html", context)
  
def categories_view(request,main, sub):
    context={}
    if request.GET.get('q'):
        context=general_searsh(request, 'c') 
    else:
        data=categorys.objects.filter(main_cat__slug= main, sub_cat__slug=sub) 
        context['qwery']=data
    if request.method == "POST":
        delte(request, categorys) 
    context['qwery']=map(lambda x: {"id":x.id,'link': f"", "name": x.name, "edit":f"/shopkeeper/edit-category/{x.id}" }, context['qwery'] )
    context['main']=main.replace("-", " ")
    context['sub']=sub.replace("-", " ")
    return render(request, f"admin_pages/category.html", context)
  


def delte(request, obj):
    ids=request.POST.getlist('id[]')
    for id in ids:
        order= obj.objects.get(pk=id)
        order.delete()





def logout_admin(request):
    logout(request)
    return redirect('admin-page')
