from .cart import Cart


def cart_for_all_page(request):
    cart = Cart(request)
    return {'cart': cart}
