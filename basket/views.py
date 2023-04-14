from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from shopkeeper.models import pruduct

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        print(product_id)
        product_qty = int(request.POST.get('productqty'))
        product_color = request.POST.get('productcolor')
        product_size = request.POST.get('productsize')
        product = get_object_or_404(pruduct, id=product_id)
        basket.add(product=product, qty=product_qty, color=product_color, size=product_size)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty, 'total':basket.get_total()})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_sub_total()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal, 'total':basket.get_total()})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        baskettotal = basket.get_sub_total()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal, 'total':basket.get_total()})
        return response
