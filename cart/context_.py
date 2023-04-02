from .cart import Cart


def cart_for_all_page(request):
    '''
    this function is for all pages
    '''
    cart = Cart(request)
    return {'cart': cart}
