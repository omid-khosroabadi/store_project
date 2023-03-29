from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.MobileList.as_view(), name='mobile_list'),
    path('detail_mobile/<int:pk>/', views.MobileDetail.as_view(), name='mobile_detail'),
    path('comment_mobile/<int:pk>/', views.CommentMobile.as_view(), name='comment_mobile'),
    path('comment_book/<int:pk>/', views.CommentBook.as_view(), name='comment_book'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
]


