
### Final Documentation

- Combine all the commands and their outputs into a single file named `CRUD_operations.md`.

### Example of `CRUD_operations.md`

```markdown
# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Output (Expected)
print(book)
# Output: <Book: 1984>
