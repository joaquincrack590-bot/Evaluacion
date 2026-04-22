from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def detail_book(request, id):
    detail_book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail_book.html', {'detail_book': detail_book})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# ... tus otras vistas ...

# En books/views.py
def add_book(request):  # <--- Verifica que el nombre sea este exactamente
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        Book.objects.create(title=title, author=author, image=image)
        return redirect('home')
    return render(request, 'books/home.html')