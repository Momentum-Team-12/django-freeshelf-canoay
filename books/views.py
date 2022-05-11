from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category, Favorite 
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/list_books.html")


@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", 
                  {"books": books})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html",       
                    {"book": book})


@login_required
def oldest(request):
    books = Book.objects.order_by('created_at')
    return render(request, "books/list_books.html", 
                  {"books": books})

@login_required
def newest(request):
    books = Book.objects.order_by('-created_at')
    return render(request, "books/list_books.html", 
                  {"books": books})


@login_required
def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, "books/category.html", {"books":books, "category": category})