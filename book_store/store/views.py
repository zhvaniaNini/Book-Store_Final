
from django.shortcuts import render

from store.models import Book

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'store/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'store/book_detail.html', {'book': book})
