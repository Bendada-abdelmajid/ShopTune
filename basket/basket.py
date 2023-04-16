from decimal import Decimal

from shopkeeper.models import pruduct
from .models import OrdedrOption


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty, color, size):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            self.basket[product_id]['color'] = color
            self.basket[product_id]['size'] = size
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty , 'color': color , 'size': size}
        self.save()
        
    def __iter__(self):
       
        product_ids = self.basket.keys()
        products = pruduct.objects.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())
    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()
        
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    def get_sub_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
    def get_delevery(self):
        try:
            price= OrdedrOption.objects.all()[0].price 
        except:
            price=0
        return price
       
    def get_total(self):
        total = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
        return total + OrdedrOption.objects.all()[0].price 
    def save(self):
        self.session.modified = True
    def vide(self):
        self.session['skey'] = {}


