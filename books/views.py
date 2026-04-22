from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def detail_book(request, id):
    detail_book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail_book.html', {'detail_book': detail_book})

def add_book(request):
    return render(request, 'books/add_book.html') # Asegúrate de crear este HTML después

def edit_book(request, id):
    # Por ahora solo que cargue una página básica
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')