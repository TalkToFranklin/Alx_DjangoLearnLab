# API Documentation

## Endpoints

### List Books
- **URL**: `/api/books/`
- **Method**: `GET`
- **Permissions**: Public access

### Retrieve a Book
- **URL**: `/api/books/<int:pk>/`
- **Method**: `GET`
- **Permissions**: Public access

### Create a Book
- **URL**: `/api/books/create/`
- **Method**: `POST`
- **Permissions**: Authenticated users only
- **Request Body**:
  ```json
  {
      "title": "New Book",
      "publication_year": 2023,
      "author": 1
  }


OR

# Advanced API Project

This project demonstrates the use of Django REST Framework to handle CRUD operations with custom views and permissions.

## API Endpoints

- **/books/** (GET, POST): Retrieve all books or create a new book (POST requires authentication).
- **/books/<id>/** (GET, PUT, DELETE): Retrieve, update, or delete a specific book (PUT, DELETE require authentication).

## Testing
- Use Postman or `curl` to test the API endpoints.
- Example `curl` request to retrieve all books:

