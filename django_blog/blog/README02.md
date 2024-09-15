# Week 14 - Task 2 - Step 7 Documentation for CRUD operations

# Django Blog CRUD Features

This project includes full blog post management functionality with the following features:

1. **Create a Blog Post**: Authenticated users can create posts.
2. **Read Blog Posts**: All users (authenticated or not) can view the list and details of posts.
3. **Update a Post**: Only the author can edit their posts.
4. **Delete a Post**: Only the author can delete their posts.

## Setting Up

1. Run the development server using `python manage.py runserver`.
2. Create a new post by navigating to `/post/new/`.
3. View the list of posts at `/`.
4. Edit or delete posts through the post details page.

Make sure to run `python manage.py migrate` after making changes to the database models.
