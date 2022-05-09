from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", 
                 {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html",       
                    {"book": book})

