from django.shortcuts import render, get_object_or_404, redirect, reverse
from .cart import Cart
from products.models import Mobile
from .forms import AddToCart
from django.contrib import messages


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', context={'cart': cart})


def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Mobile, id=pk)
    form = AddToCart(request.POST)
    if form.is_valid():
        cleaned_deta = form.cleaned_data
        quantity = cleaned_deta['quantity']
        cart.add(product, quantity, replace_quantity=cleaned_deta['quantity'])
        messages.success(request, f'{product} added to cart successfully')
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Mobile, id=pk)
    cart.remove(product)
    messages.success(request, f'{product} removed from cart')
    return redirect('cart:cart_detail')


def cart_clear(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, 'your cart cleared successfully')
    else:
        messages.warning(request, 'your cart is empty')
    return redirect(reverse('products:mobile_list'))


