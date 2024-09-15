# Documentation for Django Blog Comment system

## Overview

This document outlines the comment system implemented in the Django blog project.

## Features

- **Add Comments**: Authenticated users can add comments to blog posts.
- **Edit Comments**: Users can edit their own comments.
- **Delete Comments**: Users can delete their own comments.
- **View Comments**: All users can view comments on blog posts.

## URL Patterns

- **Post Detail**: `/post/<int:pk>/` - View post and comments.
- **Comment Edit**: `/comment/<int:pk>/edit/` - Edit a comment.
- **Comment Delete**: `/comment/<int:pk>/delete/` - Delete a comment.

## Testing

To test the comment features, navigate to a blog post and try adding, editing, and deleting comments.