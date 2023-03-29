from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('clear_cart/', views.cart_clear, name='cart_clear')
]

