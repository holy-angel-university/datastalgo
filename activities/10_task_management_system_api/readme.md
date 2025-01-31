# Build a Task Management System API

The candidate will build a Task Management System API using Django and Django REST Framework. The API will allow users to create, read, update, and delete tasks, as well as filter and paginate tasks.

## Requirements

### System Features

The API should support the following features:

1. **Task Management**
   
   - Create a task
   - Retrieve a list of all tasks.
   - Retrieve details of a single task.
   - Update an existing task.
   - Delete a task.

2. **User Authentication**

    - Users must register and log in to access the API.
    - Only authenticated users can create, update, or delete tasks.
    - Users can only update or delete tasks they created.

3. **Filtering and Searching**

    - Filter tasks by status (e.g., `completed`, `in-progress`, or `pending`).
    - Search tasks by title.

4. **Pagination**

    - Implement pagination to limit the number of tasks returned in a single request.

### Models

Define the following models:

1. **User**

    - Use Django’s built-in User model for authentication.

2. **Task**

    - Fields:
      - `title` (CharField)
      - `description` (TextField)
      - `status` (CharField with choices: pending, in_progress, completed)
      - `created_by` (ForeignKey to User)
      - `created_at` (DateTimeField, auto-generated)
      - `updated_at` (DateTimeField, auto-updated)

3. **API Endpoints**

    The API should expose the following endpoints:

    1. **Authentication**
        - `POST /api/v1/register/`: Register a new user.
        - `POST /api/v1/login/`: Log in an existing user.
    2. **Tasks**
        - `GET /api/v1/tasks/`: Retrieve a list of all tasks (with filtering and pagination).
        - `POST /api/v1/tasks/`: Create a new task.
        - `GET /api/v1/tasks/<id>/`: Retrieve details of a single task.
        - `PUT /api/v1/tasks/<id>/`: Update an existing task.
        - `DELETE /api/v1/tasks/<id>/`: Delete a task.
4. **Authentication**

    - Use **Token Authentication** for securing the API.
    - Only authenticated users can create, update, or delete tasks.
    - Users can only update or delete tasks they created.

5. **Filtering and Searching**

    - Allow filtering tasks by `status` (e.g., `/api/tasks/?status=completed`).
    - Allow searching tasks by `title` (e.g., `/api/tasks/?search=task`). The search should be case-insensitive.

6. **Pagination**

    - Implement pagination to limit the number of tasks returned in a single request (e.g., 10 tasks per page).
  
7. **Error Handling**

    - Return appropriate HTTP status codes and error messages for invalid requests (e.g., 400 for bad requests, 404 for not found, 403 for unauthorized access).

## Instructions

1. **Set Up the Project**

   - Create a new Django project and app.
   - Install Django REST Framework and configure it in `settings.py`.

2. **Define Models**

   - Create the `Task` model with the required fields.
   - Run migrations to create the database tables.

3. **Implement Authentication**

   - Use DRF’s `TokenAuthentication` for user authentication.
   - Create endpoints for user registration and login.

4. **Create Serializers**

   - Define serializers for the `Task` model.
   - Include validation for task creation and updates.

5. **Build Views**

   - Use DRF’s `ModelViewSet` or `APIView` to implement the task endpoints.
   - Add permission classes to restrict access to authenticated users.

6. **Add Filtering and Searching**

   - Use DRF’s `DjangoFilterBackend` or custom filtering logic.
   - Implement search functionality using DRF’s `SearchFilter`.

7. **Implement Pagination**

   - Use DRF’s built-in pagination classes (e.g., `PageNumberPagination`).

8. **Test the API**

   - Use tools like Postman or curl to test all endpoints.
   - Ensure proper error handling and response formats.

## Expected Deliverables

1. **Code**

   - A GitHub repository containing the activity (the Django project).


---

This activity will help you identify candidates who are proficient in Django and DRF, and who can build robust, scalable APIs. It also simulates real-world tasks they might encounter in your startup, making it a practical assessment tool.