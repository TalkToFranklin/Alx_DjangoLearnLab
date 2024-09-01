# Delete Operation

```python

from bookshelf.models import Book

# Delete the book instance
book.delete()

# Try to retrieve all books
books = Book.objects.all()

# Output (Expected)
print(books)
# Output: <QuerySet []>
