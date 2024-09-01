# Django Permissions and Groups Setup

## Groups and Permissions
- **Editors:** Can create and edit books.
- **Viewers:** Can view books.
- **Admins:** Can perform all actions, including deleting books.

## Custom Permissions

In the `Book` model, the following custom permissions have been defined:

- `can_view`: Permission to view books.
- `can_create`: Permission to create new books.
- `can_edit`: Permission to edit existing books.
- `can_delete`: Permission to delete books.

## User Groups

The following groups have been created in the Django admin interface:

- **Editors**: 
  - Permissions: `can_create`, `can_edit`
  
- **Viewers**: 
  - Permissions: `can_view`
  
- **Admins**: 
  - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Setting Up Permissions
1. Define custom permissions in the model's Meta class.
2. Create groups in the Django Admin and assign appropriate permissions.
3. Use the `permission_required` decorator in views to enforce permissions.

## Enforcing Permissions in Views

Each view that modifies books checks for the corresponding permission using the `@permission_required` decorator. 

### Example Usage

- To create a book, the user must belong to the **Editors** or **Admins** group.
- To view the book list, the user must belong to the **Viewers**, **Editors**, or **Admins** group.