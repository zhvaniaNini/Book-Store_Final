from django.urls import path
from store.views import books_list, book_detail

app_name = 'store'

urlpatterns = [
    path('books/', books_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail')
]