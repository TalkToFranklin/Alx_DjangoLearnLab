# Tagging and Search Features for Django Blog

## Overview

This document outlines the tagging and search features implemented in the Django blog project.

## Features

- **Tagging**: Users can add tags to their blog posts. Tags can be clicked to filter posts by that tag.
- **Search**: Users can search for posts based on keywords in the title, content, or tags.

## URL Patterns

- **Search**: `/search/?q=<search_term>` - Search for posts.
- **Tagged Posts**: `/tags/<tag_name>/` - View posts associated with a specific tag.

## Usage

To add tags to a post, include them in the tag field when creating or editing a post. Use the search bar to find posts by keywords or tags.