# Week 11 - Enforce Permissions in Views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = get_object_or_404(Author, id=request.POST['author'])
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})












from django.shortcuts import render

# Create your views here.
