from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .models import OrderItem
from cart.cart import Cart
from .forms import OrderForm
from django.contrib import messages


@login_required
def order_list(request):
    cart = Cart(request)
    form = OrderForm()

    if len(cart) == 0:
        messages.warning(request, 'your cart is empty')
        return redirect('products:mobile_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()
            messages.success(request, 'Your order has been successfully placed')
            request.user.first_name = obj.f_name
            request.user.last_name = obj.l_name
            request.user.save()
            return redirect(reverse('products:mobile_list'))

    return render(request, 'orders/order_list.html', context={'form': form,
                                                              })
