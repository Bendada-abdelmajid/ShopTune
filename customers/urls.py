from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(sing_up_uesr, login_uesr, update_Profile, changeCustomerPassword, logout_user, ordersView, savedsView, saveProduct, addReview)


urlpatterns = [
    path('sing_up', sing_up_uesr, name='sing-up'),
    path('login', login_uesr, name='login-user'),
    path('profile/<int:pk>', update_Profile, name='profile'),
    path('change-password/', changeCustomerPassword, name='changeCustomer-Password'),
    path('customer/orders', ordersView, name='customer_orders'),
    path('customer/wish-list', savedsView, name='customer_saveds'),
    path('customer/save/<int:cust>/<int:pk>', saveProduct, name='save_product'),
    path('add-review/<int:pk>', addReview, name='add_review'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/resset_password/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/resset_password/password_reset_sent.html"), 
        name="password_reset_done"),
   path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/resset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/resset_password/password_reset_done.html"), 
        name="password_reset_complete"),
     path('logout_user', logout_user,name="logout_user"),	

]