# Social Media API

## Overview

This is a simple Social Media API built using Django and Django REST Framework.

## API Endpoints

### Posts

- **List Posts**
  - **URL**: `/api/posts/`
  - **Method**: GET
  
- **Create Post**
  - **URL**: `/api/posts/`
  - **Method**: POST 
  - **Request Body**:
  
```json
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}

Retrieve Post
- URL: /api/posts/{id}/
- Method: GET

Update Post
- URL: /api/posts/{id}/
- Method: PUT
- Request Body:

json
{
  "title": "Updated Title",
  "content": "Updated content."
}

Delete Post
- URL: /api/posts/{id}/
- Method: DELETE



Testing Instructions

### Deliverables Summary

1. **Code Files**: Include all models, serializers, views, and URL configurations related to posts and comments.
2. **API Documentation**: Detailed descriptions of each endpoint with usage examples.
3. **Testing Results**: Evidence of testing and validation using tools like Postman or automated tests.

### Conclusion 

You have successfully developed core functionalities of your Social Media API by adding posts and comments features. Users can now create, view, update, and delete their posts and comments within the social media platform. This enhances user engagement and interaction within your application! You can continue to build upon this foundation with additional features as needed.