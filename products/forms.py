from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.Form):
    '''
    for search products
    '''
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': _('search for mobile')}))


class CommentForm(forms.ModelForm):
    '''
    The fields that the user must fill in to post a comment
    '''
    class Meta:
        model = Comment
        fields = ['body', 'recommend', 'star']
