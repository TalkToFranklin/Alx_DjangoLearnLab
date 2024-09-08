from django.db import models

# Create your models here.

# Week 13 - step 3

class Author(models.Model):
    """
    Model representing an author. This model is linked to books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """
    Model representing a book. This model has a foreign key to the Author model, 
    allowing multiple books to be associated with one author.
    """
    title = models.CharField(max_length=200) # Book's title
    publication_year = models.IntegerField() # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) # One-to-many relationship

    def __str__(self):
        return self.title
    

''' 
BookListView: Lists all books and allows read access to everyone.
BookDetailView: Retrieves a single book by its ID and allows read access to everyone.
BookCreateView: Allows authenticated users to create new books.
BookUpdateView: Allows authenticated users to update existing books.
BookDeleteView: Allows authenticated users to delete books.
'''