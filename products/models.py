from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext as _


class Mobile(models.Model):
    '''
    Mobile product information
    '''
    COLORS = (
        ('GREEN', _('green')),
        ('YELLOW', _('yellow')),
        ('BLUE', _('blue')),
        ('RED', _('red')),
        ('BROWN', _('brown')),
        ('WHITE', _('white')),
        ('BLACK', _('black')),
    )
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='mobile_image/')
    weight = models.PositiveIntegerField()
    colors = MultiSelectField(choices=COLORS, max_length=200)
    datetime_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:mobile_detail', args=[self.id])


class Book(models.Model):
    '''
    Book product information
    '''
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = RichTextField()
    image = models.ImageField(upload_to='book_image/', blank=True, default='static/img/No-Image.jpg')
    price = models.PositiveIntegerField(default=0)
    datetime_created = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('products:book_detail', args=[self.id])


class Comment(models.Model):
    '''
    Fields related to sending comments
    '''
    STAR = (
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect')),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_book', null=True, blank=True)
    body = models.TextField()
    recommend = models.BooleanField(default=True)
    star = models.CharField(max_length=200, choices=STAR)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('products:mobile_detail', args=[self.mobile.id])

