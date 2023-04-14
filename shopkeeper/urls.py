from django.urls import path
from .views import (adminPage, addTodo, deleteTodo, order_detail,
 main_categories_view, sub_categories_view, categories_view, AddPruduct, AddColor, AddMainCategory, AddSubCategory,
  AddCategory,editMainCategory, editSubCategory, editCategory, get_notifs, order_hasSeen, order_hascomplet, change_state, Product_view,
    allOreders_view, editProduct, editCategory, add_more_info,  change_password,
    order_category_summary, logout_admin, delete_order)

urlpatterns = [
    path('admin_page', adminPage, name='admin-page'),

    path('get_notifs', get_notifs, name='get-notifs'),
    path('add_todo', addTodo, name='add-todo'),
    path('delete_todo/<int:pk>', deleteTodo, name='delete-todo'),
    path('has_seen /<int:pk>', order_hasSeen, name='has-seen'),
    path('has_complet/<int:pk>', order_hascomplet, name='has-complet'),
    path('order-detail/<int:pk>', order_detail, name='order-detail'),
    path('add-pruduct', AddPruduct, name='add-pruduct'),
    path('add-color', AddColor, name='add-color'),
    path('add-main-category', AddMainCategory, name='add-main-category'),
    path('add-sub-category', AddSubCategory, name='add-sub-category'),
    path('add-category', AddCategory, name='add-category'),
    path('edit-main-category/<int:pk>', editMainCategory, name='edit-main-category'),
    path('edit-sub-category/<int:pk>', editSubCategory, name='edit-sub-category'),
    path('edit-category/<int:pk>', editCategory, name='edit-category'),
    path('edit-product/<int:pk>', editProduct, name='edit-product'),
   
    path('products', Product_view, name='products'),
    path('change-state/<int:pk>', change_state, name='change-state'),
    path('categories', main_categories_view, name='main-category'),
    path('categories/<str:main>', sub_categories_view, name='sub-categories'),
    path('categories/<str:main>/<str:sub>',
         categories_view, name='categories'),
    path('orders', allOreders_view, name='orders'),
    path('orders/delete-order/<int:pk>', delete_order, name='delete-order'),

    path('Profiel/<int:pk>', add_more_info, name='profiel'),
    path('change_password', change_password, name='change-password'),
    path('order_category_summary/<str:type>', order_category_summary,
         name="order_category_summary"),

    path('logout_admin', logout_admin, name="logout_admin"),

]
