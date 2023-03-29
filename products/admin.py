from django.contrib import admin
from .models import Mobile, Comment, Book


class CommentMobileUnder(admin.TabularInline):
    model = Comment
    fields = ['user', 'body', 'star', 'recommend']
    extra = 1


class CommentBookUnder(admin.TabularInline):
    model = Comment
    fields = ['user', 'body', 'star', 'recommend']
    extra = 1


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'colors']
    inlines = [
        CommentMobileUnder,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'recommend', 'body', 'star']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [
        CommentBookUnder,
    ]


