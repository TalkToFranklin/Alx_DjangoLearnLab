# Django Admin Configuration for the Book Model

# Step 1: Register the Book Model

1. Open `bookshelf/admin.py`.
2. Add the following code to register the `Book` model:

   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       list_filter = ('author',)
       search_fields = ('title', 'author')

# Step 2: Customize the Admin Interface



# Step 3: Access the Admin Interface

"""
- Run python manage.py runserver
- Open http://127.0.0.1:8000/admin/ in your web browser.
- Log in with your superuser account.
- Manage the Books entries through the admin interface. """




# Step 4: