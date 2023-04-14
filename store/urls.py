from django.urls import path
from .views import storView, search_json, cardView,products, mainCatView,subCatView,CatView, checkoutView, succes_view

urlpatterns = [
    path('', storView , name='home'),
   
    path('search-json/', search_json , name='search_json'),
    path('product/<str:slug>', cardView , name='product'),

  
    path('products/', products , name='all-products'),
    path('products/<str:main>', mainCatView , name='main-cats'),
    path('products/<str:main>/<str:sub>', subCatView , name='sub-cats'),
    path('products/<str:main>/<str:sub>/<str:cat>', CatView , name='cat-cats'),
   
    path('checkout', checkoutView, name='checkout'),
  
    path('checkout/success', succes_view, name='success'),
]