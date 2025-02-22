# RESTful API

The goal is to provide variety and a good level of challenge while reinforcing
the CRUD principles.

## General Requirements

- **Technology**: Use Django and Django REST Framework.
- **Functionality**: Implement RESTful API endpoints for CRUD operations
  (Create, Read, Update, Delete).
- **Endpoints**: Use standard RESTful URL patterns:
  - `/api/v1/{resource}/` (for list and create - GET and POST methods)
  - `/api/v1/{resource}/{id}/` (for detail, update, delete - `GET`,
    `PUT`/`PATCH`, `DELETE` methods)
- **Model**:
  - It should have at least 10 fields, including a primary key, `id`.
  - Each field should have appropriate data types and constraints.
  - Implement custom validation for fields as needed.
  - Should have timestamps for `created_at` and `updated_at`.
- **Serialization**: Create appropriate serializers to handle data conversion to
  and from JSON.
- **Views**: Implement view functions to handle requests and responses, calling
  service functions.
- **Services**: Create a service layer to encapsulate business logic and
  database interactions.
- **Testing**: Test all API endpoints using Postman, document it properly.

## Instructions

1. You only have two (2) hours to complete the task.
2. Each group consist only 2 members. Each group will present their work.
3. Commit your work to your GitHub repository, publicly.
4. Submit your repository link to this **[link](https://docs.google.com/spreadsheets/d/1ctOYIgukdJZTlD2uVBPJ5FRpk5KxfqoZlptOrThXNyk/edit?usp=sharing)** once you're done.

### Criteria

Students who will be presenting their work will be graded based on the following
criteria:

- **Functionality**
  - Create, Read, Update, Delete operations are working.
  - Properly implemented RESTful API endpoints.
- **Serialization**
- **Views**
- **Services**
- **Testing**
- **Documentation**
  - Properly documented API endpoints.
  - Properly documented Postman tests.

## Activity Ideas & Requirements

1.  Book API

    - Suggested Models: `Book` (fields: `title`, `author`, `isbn` (unique), `publication_year`, `genre`).
    - Challenges:
      - Validate that `publication_year` is a 4-digit number and not in the
        future. Return custom error messages for invalid input.
      - Implement pagination for the book list (e.g., using PageNumberPagination
        in DRF) and allow ordering by `publication_year` or `title`.
      - Add a `is_available` (BooleanField, default True) field. Create a custom
        API endpoint `/api/v1/books/{id}/toggle_availability/` (using a `@action`
        in a ViewSet or custom URL + view function if not using ViewSet) that
        toggles the `is_available` status of a book.

2.  Movie API

    - Suggested Models: `Movie` (fields: `title`, `director`, `release_year`, `rating`).
    - Challenges:
      - Validate that `rating` is between 0 and 10 (inclusive) in the serializer.
      - Implement a more advanced search that can search by title, director, and
        genre (add `genre` field). Use DRF's `SearchFilter` but customize it to
        search across multiple fields.
      - Create a custom list API endpoint `/api/v1/movies/top_rated/` (using
        `@action` or custom URLs) that returns only movies with a rating of 8.0 or
        higher, ordered by rating in descending order.

3.  Product API

    - Suggested Models: `Product` (fields: `name`, `description`, `price`, `is_available`, `category`).
    - Challenges:
      - Ensure that the combination of `name` and `category` is unique (prevent
        duplicate product entries within the same category). Handle potential
        uniqueness errors gracefully and return appropriate error responses.
      - A llow filtering products by a price range (e.g., `/api/v1/products/?min_price=10&max_price=50`).
      - Add a `stock_level` (IntegerField) field. Make this field read-only in the API output (using `read_only=True` in the serializer) and explain why this might be useful in a real inventory system (it might be calculated based on stock movements, not directly editable via the API).

4.  Task API

    - Suggested Models: `Task` (fields: `title`, `description`, `due_date`, `is_completed`, `priority`).
    - Challenges:
      - Validate that `due_date` cannot be in the past when creating a new task.
      - Instead of directly updating `is_completed` via PUT/PATCH, create a dedicated API endpoint `/api/v1/tasks/{id}/complete/` (POST method) to mark a task as complete and `/api/v1/tasks/{id}/reopen/` (POST method) to mark it as not completed.
      - Set the default ordering for the task list to be by `due_date` (ascending) and then by `priority` (High, Medium, Low).

5.  Event API

    - Suggested Models: `Event` (fields: `name`, `description`, `start_datetime`, `location`, `category`).
    - Challenges:
      - If you add an `end_datetime` field, validate that `end_datetime` is always after `start_datetime`.
      - Allow filtering events by both `category` and date range simultaneously (e.g., events in "Music" category happening next week).
      - Create a custom list endpoint `/api/v1/events/upcoming/` that returns events starting in the next 7 days, ordered by `start_datetime`.

6.  Contact API

    - Suggested Models: `Contact` (fields: `first_name`, `last_name`, `email`, `phone_number`, `relationship`).
    - Challenges:
      - Allow multiple valid email formats (e.g., using a more robust email validator if needed) and return a specific error message if the email is invalid.
      - Allow searching contacts by full name (e.g., if you search "John Doe", it should match contacts where first name is "John" and last name is "Doe", or "John Doe" is in either first or last name).
      - Restrict updates to only allow PATCH requests for updating `phone_number` and `relationship`. `PUT` requests should still be required to update all fields including `first_name`, `last_name`, and `email`.

7.  Recipe API

    - Suggested Models: `Recipe` (fields: `name`, `ingredients`, `instructions`, `cuisine`, `dietary_restriction`).
    - Challenges:
      - Instead of `ingredients` as TextField, change it to a JSONField or similar that can store a list of ingredients. Modify serializer and views to handle list input for ingredients during creation and update.
      - Implement a search feature that finds recipes that include all of the ingredients provided in a search query (e.g., `/api/v1/recipes/?ingredients=chicken,onion,garlic`).
      - Add a `is_favorite` (BooleanField, default False) field. Create a custom action endpoint `/api/v1/recipes/{id}/favorite/` (POST) and `/api/v1/recipes/{id}/unfavorite/` (POST) to toggle `is_favorite`.

8.  BlogPost API

    - Suggested Models: `BlogPost` (fields: `title`, `content`, `author`, `publication_date`, `category`).
    - Challenges:
      - Prevent setting `publication_date` to a future date during creation or update.
      - Allow filtering blog posts by `category` and a `publication_date` range.
      - Add a `word_count` (IntegerField) field. Make this field read-only and calculate its value dynamically based on the `content` field whenever a BlogPost is retrieved or listed (using a serializer method field or similar approach).

9.  Course API

    - Suggested Models: `Course` (fields: `title`, `description`, `instructor`, `start_date`, `end_date`, `level`).
    - Challenges:
      - Validate that `end_date` is always after `start_date`.
      - Allow filtering courses by both `instructor` and `level`.
      - Add a `read-only` field in the serializer called `duration_days` that calculates and displays the duration of the course in days based on `start_date` and `end_date`.

10. Coupon API

    - Suggested Models: `Coupon` (fields: `code` (unique), `discount_percentage`, `is_active`, `expiry_date`, `usage_count` (read-only)).
    - Challenges:
      - Validate that `expiry_date` cannot be set to a date in the past during creation or update.
      - Allow filtering coupons to show only active coupons or only expired coupons (e.g., `/api/v1/coupons/?status=active` or `/api/v1/coupons/?status=expired`). You will need to define "expired" based on the current date and `expiry_date`.
      - Create a custom action endpoint `/api/v1/coupons/{id}/deactivate/` (POST) to set `is_active` to False.

11. Classroom API

    - Suggested Models: `Classroom` (fields: `name`, `capacity`, `location`).
    - Challenges:
      - Validate that `capacity` is always a positive integer.
      - Allow filtering classrooms by `location` and `capacity` range (e.g., classrooms in "Building A" with capacity between 20 and 50).
      - Create a custom action endpoint `/api/v1/classrooms/{id}/is_available/` (GET method, possibly taking `start_time` and `end_time` as query parameters) that returns whether the classroom is available during the specified time slot (based on existing bookings).

12. Meeting API

    - Suggested Models: `Meeting` (fields: `title`, `description`, `start_datetime`, `end_datetime`, `attendees`).
    - Challenges:
      - Validate that `end_datetime` is after `start_datetime` and `start_datetime` is not in the past.
      - Allow filtering meetings that include a specific attendee (search within the `attendees` TextField, which is comma-separated).
      - Add a read-only field in the serializer called `duration_minutes` that calculates and displays the duration of the meeting in minutes based on `start_datetime` and `end_datetime`.

13. City API

    - Suggested Models: `City` (fields: `name`, `country`, `population`, `latitude`, `longitude`).
    - Challenges:
      - Validate that `latitude` is between -90 and 90, and `longitude` is between -180 and 180.
      - Allow filtering cities by `country` and `population` range.
      - Requires adding a 'continent' CharField to the model. Create an endpoint `/api/v1/cities/continent/{continent_name}/` that returns all cities in a specific `continent`.

14. Superhero API

    - Suggested Models: `Superhero` (fields: `name`, `secret_identity`, `power`, `is_villain`).
    - Challenges:
      - Ensure that `name` is always provided and not blank when creating a superhero.
      - Allow searching superheroes by both `name` and `power` simultaneously.
      - Create two endpoints: `/api/v1/superheroes/villains/` and `/api/v1/superheroes/heroes/` (custom URLs and view functions) that return only villains and only heroes respectively, based on the `is_villain` field.

15. Game API

    - Suggested Models: `Game` (fields: `title`, `genre`, `release_year`, `platform`).
    - Challenges:
      - Validate `release_year` as a 4-digit year.
      - Allow filtering games by both `genre` and `platform`.
      - Create an endpoint `/api/v1/games/platform/{platform_name}/` that returns all games available on a specific `platform`.

16. Joke API

    - Suggested Models: `Joke` (fields: `setup`, `punchline`, `category`, `rating`).
    - Challenges:
      - Validate that `rating` is always between 1 and 5 (inclusive), if provided.
      - Allow filtering jokes by `category`.
      - Create an endpoint `/api/v1/jokes/top_rated/` that returns the top 10 highest rated jokes (order by `rating` descending, handle null ratings – maybe exclude them or treat them as lowest rating).

17. Quote API

    - Suggested Models: `Quote` (fields: `text`, `author`, `source`, `year`).
    - Challenges:
      - Ensure `text` is not blank and has a minimum length (e.g., at least 10 characters).
      - Allow filtering quotes by both `author` and `year` range.
      - Create an endpoint `/api/v1/quotes/author/{author_name}/` that returns all quotes by a specific author.

18. Color API

    - Suggested Models: `Color` (fields: `name`, `hex_code` (unique), `rgb_value`, `is_favorite_color`).
    - Challenges:
      - Validate that `hex_code` is in a valid hexadecimal color code format (e.g., starts with '#' and followed by 6 hexadecimal characters).
      - Allow ordering colors alphabetically by `name`.
      - Create an endpoint `/api/v1/colors/favorites/` that returns only colors where `is_favorite_color` is True.
