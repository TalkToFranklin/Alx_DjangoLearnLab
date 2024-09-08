# API Testing Documentation

## Overview

This document outlines the testing strategy for the API endpoints in the `advanced_api_project`. The tests focus on CRUD operations for the `Book` model and verify the functionality of filtering, searching, and ordering.

## Test Cases

### 1. Create Book
- **Test**: Ensure a new book can be created.
- **Expected Outcome**: HTTP 201 Created and the book is saved in the database.

### 2. Update Book
- **Test**: Ensure an existing book can be updated.
- **Expected Outcome**: HTTP 200 OK and the book's details are updated.

### 3. Delete Book
- **Test**: Ensure a book can be deleted.
- **Expected Outcome**: HTTP 204 No Content and the book is removed from the database.

### 4. List Books
- **Test**: Ensure all books can be listed.
- **Expected Outcome**: HTTP 200 OK and the correct number of books are returned.

### 5. Filter Books
- **Test**: Ensure books can be filtered by title.
- **Expected Outcome**: HTTP 200 OK and the correct book is returned.

### 6. Search Books
- **Test**: Ensure books can be searched by title.
- **Expected Outcome**: HTTP 200 OK and the correct book is returned.

### 7. Order Books
- **Test**: Ensure books can be ordered by title.
- **Expected Outcome**: HTTP 200 OK and the books are returned in the correct order.

## Running the Tests
Run the following command to execute the tests:
```bash
python manage.py test api


OR

## Testing API Endpoints

### Running Tests

To run the unit tests for the API endpoints, use the following command:

```bash
python manage.py test api
