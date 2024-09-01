# Configure URL Patterns

from django.urls import path
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('books/', book_list, name='book_list'),  # URL for the function-based view
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('register/', views.register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # URL for user logout
]



# Implement Role-Based Access Control in Django

# Step 3 = Configure URL Patterns

# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout, admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin_view, name='admin_view'),  # URL for Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # URL for Librarian view
    path('member/', member_view, name='member_view'),  # URL for Member view
]





# Implementing Custom Permissions in Django

#Step 3 (Define URL Patterns for Secured Views)

# relationship_app/urls.py

from django.urls import path
from .views import book_list, LibraryDetailView, register, user_login, user_logout, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # URL for editing a book
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),  # URL for deleting a book
]