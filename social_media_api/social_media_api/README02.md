# Social Media API > README for user follows and feed functionality

## Overview

This is a simple Social Media API built using Django and Django REST Framework.

## API Endpoints

### Follow Management

- **Follow User**
  - **Endpoint**: `/api/accounts/follow/<int:user_id>/`
  - **Method**: POST 
  - **Request Body**: None (requires authentication)

- **Unfollow User**
  - **Endpoint**: `/api/accounts/unfollow/<int:user_id>/`
  - **Method**: POST 
  - **Request Body**: None (requires authentication)

### Feed

- **User Feed**
  - **Endpoint**: `/api/posts/feed/`
  - **Method**: GET 
  - **Response**: Returns posts from users that the authenticated user follows.

## Testing Instructions

To test the API endpoints, use tools like Postman or curl to send requests to the specified URLs.