from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Mobile, Comment, Book
from django.views import generic
from django.contrib import messages
from .forms import CommentForm
from typing import Type
from django.urls import reverse_lazy, reverse


class MobileList(generic.ListView):
    paginate_by = 3
    template_name = 'products/mobile_list.html'
    model = Mobile
    context_object_name = 'mobiles'
    mobiles = []

    def get_queryset(self):
        query_name = self.request.GET.get('query', '')
        mobile_list = Mobile.objects.filter(
            Q(title__icontains=query_name)
        )
        if len(mobile_list):
            return mobile_list
        else:
            messages.warning(self.request, 'this mobile does not exist')


class MobileDetail(generic.DetailView):
    model = Mobile
    template_name = 'products/mobile_detail.html'
    context_object_name = 'mobile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class BookList(generic.ListView):
    paginate_by = 3
    model = Book
    template_name = 'products/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query_name = self.request.GET.get('query', '')
        book_list = Book.objects.filter(
            Q(title__icontains=query_name)
        )
        if len(book_list):
            return book_list
        else:
            messages.warning(self.request, 'this book does not exist')


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'products/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_book'] = CommentForm()
        return context


class CommentMobile(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        pk = self.kwargs['pk']
        mobile = get_object_or_404(Mobile, id=pk)
        obj.mobile = mobile
        return super().form_valid(form)


class CommentBook(generic.CreateView):
    model: Type[Comment]
    form_class = CommentForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        pk = self.kwargs['pk']
        book = get_object_or_404(Book, id=pk)
        obj.book = book
        return super().form_valid(form)
