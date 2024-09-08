# API Documentation

## Filtering, Searching, and Ordering

### Endpoints

#### List Books
- **URL**: `/api/books/`
- **Method**: `GET`
- **Permissions**: Public access

### Filtering
You can filter books using the following query parameters:
- `title`: Filter by book title.
- `author__name`: Filter by author name.
- `publication_year`: Filter by the year of publication.

### Searching
You can search for books using the `search` query parameter:
- `search`: Search by book title or author name.

### Ordering
You can order the results using the `ordering` query parameter:
- `ordering`: Order by `title` or `publication_year`.

### Example Requests
- **Filter by Title**: `/api/books/?title=Harry`
- **Search by Title**: `/api/books/?search=Harry`
- **Order by Title**: `/api/books/?ordering=title`