from django import forms


class AddToCart(forms.Form):
    '''
    This function is to get the product number from the user
    '''
    QUANTITY = ((i, str(i)) for i in range(1, 11))
    quantity = forms.TypedChoiceField(choices=QUANTITY, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
