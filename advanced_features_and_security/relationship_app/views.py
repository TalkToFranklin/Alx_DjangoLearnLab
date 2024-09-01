from django.shortcuts import render

# Create your views here.

# relationship_app/views.py

from django.shortcuts import render
from .models import Book, Library
from django.views import View
from django.views.generic import ListView

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    
    # Define the template as a string

    html = '''
    <!-- list_books.html -->
    <!DOCTYPE html> 
    <html lang="en"> 
    <head> 
        <meta charset="UTF-8">
        <title>List of Books</title>
    </head>
    <body> 
        <h1>Books Available:</h1> 
        <ul>
            {% for book in books %}
            <li>{{ book.title }} by {{ book.author.name }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''
    
    return render(request, 'relationship_app/list_books.html', {'html': html})


# Class-based view to display details of a specific library
from .models import Library
from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    def get(self, request, library_id):
        library = Library.objects.get(id=library_id)  # Fetch the library by ID
        books = library.books.all()  # Get all books in that library
        
        # Define the template as a string

        html = f'''
        <!-- library_detail.html -->
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Library Detail</title>
        </head>
        <body>
            <h1>Library: {{ library.name }}</h1>
            <h2>Books in Library:</h2>
            <ul>
                {% for book in library.books.all %}
                <li>{{ book.title }} by {{ book.author.name }} (Published {{ book.publication_year }})</li>
                {% endfor %}
            </ul>
        </body>
        </html>

        '''

        
        return render(request, 'relationship_app/library_detail.html', {'html': html})







# Implementing User Authentication in Django

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Library
from django.views import View

# Function-based view to register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book_list')  # Redirect to book list after registration
    else:
        form = UserCreationForm()

    html = '''
    <!-- register.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Register</title>
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>
    <body>
        <h1>Register</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Register</button>
        </form>
    </body>
    </html>
    '''
    return render(request, 'relationship_app/register.html', {'html': html})

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(View):
    def get(self, request, library_id):
        library = Library.objects.get(id=library_id)  # Fetch the library by ID
        books = library.books.all()  # Get all books in that library
        return render(request, 'relationship_app/library_detail.html', {'library': library, 'books': books})

# Function-based view for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')  # Redirect to book list after successful login
    
    html = '''
    <!-- login.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>
    <body>
        <h1>Login</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
        <a href="{% url 'register' %}">Register</a>
    </body>
    </html>
    '''
    return render(request, 'relationship_app/login.html', {'html': html})

# Function-based view for user logout
def user_logout(request):
    html = '''
    <!-- logout.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>User Logout</title>
    </head>
    <body>
        <h1>You have been logged out.</h1>
        <a href="{% url 'login' %}">Login again</a>
    </body>
    </html>
    '''
    return render(request, 'relationship_app/logout.html', {'html': html})






# Implement Role-Based Access Control in Django

# Set Up Role-Based Views

# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')







# Implementing Custom Permissions in Django

#Step 2 ( Update Views to Enforce Permissions) 

# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# Function to add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('book_list')  # Redirect to book list after adding
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

# Function to edit an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = get_object_or_404(Author, id=request.POST['author'])
        book.save()
        return redirect('book_list')  # Redirect to book list after editing
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

# Function to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})

