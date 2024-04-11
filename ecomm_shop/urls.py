from django.urls import path
from ecomm_shop import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_account/', views.user_delete, name='del_account'),
    path('update_account/', views.user_update, name='update_account'),
    path('cart_items/', views.cart_items, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('decrease-cart-item/<int:cart_item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('terms_and_conditions/', views.terms, name='terms'),

]
