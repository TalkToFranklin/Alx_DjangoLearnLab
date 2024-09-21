# Social Media API

## Overview

This is a Social Media API built using Django and Django REST Framework.

## API Endpoints

### Likes

- **Like Post**
  - **Endpoint**: `/api/posts/<int:id>/like/`
  - **Method**: POST 
  - **Request Body**: None (requires authentication)

- **Unlike Post**
  - **Endpoint**: `/api/posts/<int:id>/unlike/`
  - **Method**: POST 
  - **Request Body**: None (requires authentication)

### Notifications

- **Get Notifications**
  - **Endpoint**: `/api/notifications/`
  - **Method**: GET 
  - **Response**: Returns a list of notifications for the authenticated user.

## Testing Instructions

To test the API endpoints, use tools like Postman or curl to send requests to the specified URLs.