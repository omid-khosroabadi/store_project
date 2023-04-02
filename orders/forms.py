from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
    This function is to get user profile
    '''
    class Meta:
        model = Order
        fields = ['f_name', 'l_name', 'phone', 'address', 'description']
        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'placeholder': 'enter somthing'}),
        }
