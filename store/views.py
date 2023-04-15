

import os
from django.shortcuts import render, redirect, get_object_or_404

from shopkeeper.models import pruduct, categorys, subCat, mainCat
from basket.models import Ordedr,  OrdedrItem, OrdedrOption
from basket.basket import Basket

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from decimal import Decimal
from customers.models import Customer
from django.contrib.auth.models import User
# Create your views here.


def storView(request):
    cats = []
    products = pruduct.objects.all().order_by('-views')[:20]
    for p in products:
        cats.append(p.category)
    cats = list(set(cats))
    print("start site ")
    print("elow world ")
    new_products = pruduct.objects.all().order_by('product_date')[:5]
    offers_products = pruduct.objects.exclude(
        discount=None).order_by('discount')[:3]
    return render(request, 'stor.html', {"products": products, "new_prods": new_products, "offer_prods": offers_products, "cats": cats})


def cardView(request, slug):
    prod = get_object_or_404(pruduct, slug=slug)
    prod.views += 1
    prod.save()
    ratings={0:[0,0],1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0] }
    rtings_list=[]
    
    for x in prod.riviews.all():
        rtings_list.append(x.rate)
  

    for r in rtings_list:
        ratings[r]=[rtings_list.count(r), (rtings_list.count(r) / len(rtings_list))*100]
    print(ratings)
    
    k=0
    l=0
    for r , i in ratings.items():
        k+=r*i[0]
        l+=i[0]

    print(k)
    print(l)
    try:
        total_rate=k/l
        total_persntage=total_rate / 5 *100
    except:
        total_rate=0
        total_persntage=0
    
    products = pruduct.objects.filter(category=prod.category)
    
    cats=categorys.objects.filter(sub_cat=prod.category.sub_cat)
    print(prod.category.sub_cat.id)
  
    return render(request, 'card.html', {'prod': prod, 'products': products,"cats":cats, "ratings": ratings, "num":len(rtings_list),"total_rate":total_rate, "total_persntage":total_persntage})


def pagination(products):
    index = products.number - 1
    length = len(products.paginator.page_range)
    start_index = index - 1 if index >= 1 else 0
    if index == length - 1:
        start_index = index - 2
    elif index >= 1:
        start_index = index - 1
    else:
        end_index = 0
    end_index = length
    if index == 0:
        end_index = index + 3
    elif index <= length - 2:
        end_index = index + 2
    else:
        end_index = length
    page_range = products.paginator.page_range[start_index:end_index]
    return page_range



def explore(request, main, sub, cat):

    products = []
    links = []
    title = ""
    main_link = None
    sub_link = None
    if not main and not sub and not cat:
        if request.GET.get('search'):
            q = request.GET.get('search')
            title = "Search  "+q
            products= pruduct.objects.filter(Q(title__icontains=q) | Q(category__name__icontains=q))
        else:
            main_cats = mainCat.objects.all()
            title = "All Products"
            for m in main_cats:
                links.append({"name": m.name, "link": "/products/"+m.slug})
            products = pruduct.objects.all()
    elif main and not sub and not cat:
        main_cat = mainCat.objects.get(slug=main)
        title = main.replace("-", " ")
        sub_cats = subCat.objects.filter(main_cat=main_cat.id)
        cats = categorys.objects.filter(main_cat=main_cat.id)
        for sub_cat in sub_cats:
            links.append(
                {"name": sub_cat.name, "link": "/products/"+main+"/"+sub_cat.slug})

        products = pruduct.objects.filter(category__in=cats)
    elif sub and not cat:
        main_cat = mainCat.objects.get(slug=main)
        sub_cat = subCat.objects.get(main_cat=main_cat.id, slug=sub)
        cats = categorys.objects.filter(sub_cat=sub_cat.id)
        main_link = main.replace("-", " ")
        title = sub.replace("-", " ")
        for cat in cats:
            links.append(
                {"name": cat.name, "link": "/products/"+main+"/"+sub+"/"+cat.slug})
        products = pruduct.objects.filter(category__in=cats)

    elif cat:
        main_link = main.replace("-", " ")
        sub_link = sub.replace("-", " ")
        category = categorys.objects.get(slug=cat)
        title = cat.replace("-", " ")
        products = pruduct.objects.filter(category=category)
    filters = getFiltters(products)
    order = "Popularity"
    filrs = []
    if request.GET.get('color') or request.GET.get('size'):

        for f in dict(request.GET.lists()).values():
            filrs.extend(f)
        print(filrs)
        products = products.filter(Q(colors__name__in=filrs) | Q(size__in=filrs) | Q(
            size2__in=filrs) | Q(size3__in=filrs) | Q(size4__in=filrs))

    if request.GET.get('min-price') and request.GET.get('max-price'):
        min_price = Decimal(request.GET.get('min-price'))
        max_price = Decimal(request.GET.get('max-price'))
        products = products.filter(price__gte=min_price, price__lte=max_price)
    if request.GET.get('availability'):
        if request.GET.get('availability') == "true":
            products = products.filter(out_of_stock=False)
        else:
            products = products.filter(out_of_stock=True)
    
    if request.GET.get('order') == 'new':
        order = "Fresh Arrivals"
        products = products.order_by("product_date")
    elif request.GET.get('order') == 'discount':
        order = "Discount"
        products = products.order_by("-discount")
    elif request.GET.get('order') == 'popular':
        order = "Popularity"
        products = products.order_by("-views")
    elif request.GET.get('order') == 'low-price':
        order = "Price Low To High"
        products = products.order_by("price")
    elif request.GET.get('order') == 'high-price':
        order = "Price High To Low"
        products = products.order_by("-price")

    return render(request, 'explore.html', {'products': products, "main": main_link, "sub": sub_link, "search":request.GET.get('search'),'title': title,  'links': links, "colors": filters['colors'], "sizes": filters['sizes'], "min_price": filters['min_price'], "max_price": filters['max_price'], "order": order, "filters": filrs, "availability": request.GET.get('availability')})


def products(request):
    return explore(request, None, None, None)


def mainCatView(request, main):
    return explore(request, main, None, None)


def subCatView(request, main, sub):
    return explore(request, main, sub, None)


def CatView(request, main, sub, cat):
    return explore(request, main, sub, cat)




def search_json(request):
    q = request.GET.get('q')
    search = []
    search_products = pruduct.objects.filter(title__icontains=q)[:8]
    for prod in search_products:
        
        search.append({"title": prod.title, "slug": prod.slug, "price": prod.price,"oldprice":prod.oldprice ,
                      "discount": prod.discount, "img": prod.image.all()[0].image.url})
    data = {"search": search}
    print(data)
    return JsonResponse(data, safe=False)


def checkoutView(request):
    clientID =  os.environ.get('CLIENT_ID') 
   

    basket = Basket(request)
    if request.user.is_authenticated and basket:
        orderOptions = OrdedrOption.objects.all()
        if request.method == "POST" and request.POST.get('address') and request.POST.get('country') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('abdhvsdhgsvdhs'):
        
            delvery=OrdedrOption.objects.get(id=request.POST.get('order_option'))  
            user=User.objects.get(id= request.user.id)

            print(user)
            new_order = Ordedr.objects.create(customer=request.user, address=request.POST.get('address'), contry=request.POST.get('country')
            , city=request.POST.get('city'), postal=request.POST.get('postal_code'),ordedrOption=delvery,   total_price=Decimal(request.POST.get('abdhvsdhgsvdhs')) )
            print("aftter user new order")
            print(new_order)
            for p in basket:
                if 'color' in p:
                    color = p['color']
                else:
                    color = ""
                if 'size' in p:
                    size = p['size']
                else:
                    size = ""

                new_orederItem = OrdedrItem.objects.create(
                    product=p['product'], price=p['total_price'], qty=p['qty'], color=color, size=size)
                new_orederItem.save()
                print(new_orederItem)
                new_order.add_order(new_orederItem)
                print(new_order)

            new_order.save()
            print(new_order)
          
            basket.vide()
            return redirect("success")
        return render(request, 'checkout.html', {"orderOptions": orderOptions, "clientID": clientID})
    else:
        return redirect("home")


def succes_view(request):
    done = request.session.get('success')
    request.session['success'] = ''
   

    return render(request, 'succes.html', {'done': done})


def getFiltters(products):
    colors = []
    sizes = []
    min_price = 0
    max_price = 0
    if products:
        min_price = products[0].price
        max_price = products[0].price
        for p in products:
            s = p.get_sizes()
            colors.extend(p.colors.all())
            sizes.extend(s)
            if p.price < min_price:
                min_price = p.price
            if p.price > max_price:
                max_price = p.price
    
    
   

    return {"colors": list(set(colors)), "sizes": list(set(sizes)), "min_price": min_price, "max_price": max_price}
