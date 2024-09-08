# Retrieve Operation

```python
# Retrieve the book instance
book = Book.objects.get(title="1984")

# Output (Expected)
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Output: Title: 1984, Author: George Orwell, Year: 1949
