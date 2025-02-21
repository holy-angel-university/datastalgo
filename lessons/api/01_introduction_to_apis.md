# Introduction to APIs

## What is an API?

An API (Application Programming Interface) is like a waiter in a restaurant. It
takes requests from a client (like a web application, mobile app, or another
service), gets the data from the server (database), and sends back the response
in a structured format (usually JSON for web APIs).

So, traditional web applications often return HTML to be rendered in a browser.
APIs return data (often JSON) to be used by other applications.

> Sample Diagram: client → API → Database → API → client

## Why APIs?

- Data sharing between different applications (web, mobile, partners).
- Building decoupled systems (front-end and back-end can be developed
  independently).
- Enabling reusable services.

## Introduction to REST and RESTful APIs

### REST

REST (Representational State Transfer) is an architectural style for designing
networked applications. It relies on a stateless, client-server communication
protocol, almost always HTTP.

#### Example of a REST API

##### Endpoints

| Method | URL           | Description         |
| ------ | ------------- | ------------------- |
| GET    | /api/v1/users | Get all users       |
| GET    | /users/{id}   | Get a user by ID    |
| POST   | /users        | Create a new user   |
| PUT    | /users/{id}   | Update a user by ID |
| DELETE | /users/{id}   | Delete a user by ID |

##### Request/Response

1. Get All Users

Request

```http
GET /users HTTP/1.1
Host: api.example.com
```

Response

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com"
  }
]
```

1.  Create a User

Request

```http
POST /users HTTP/1.1
Content-Type: application/json

{
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

Response

```json
201 Created

{
  "id": 3,
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

### RESTful APIs

These are APIs that adhere to the REST architectural constraints. They are
designed to be simple, consistent, and easy to use.

#### Example of a RESTful API

Key differences

- Uses proper resource naming (e.g., `/users` instead of `/getUsers`).
- Uses standard HTTP response codes (e.g., `200 OK`, `201 Created`,
  `404 Not Found`).
- Uses HTTP methods (GET, POST, PUT, DELETE) to perform operations.
- Stateless (each request contains all necessary info)

##### Endpoints

| Method | URL               | Description                      |
| ------ | ----------------- | -------------------------------- |
| GET    | /users            | Get all users                    |
| GET    | /users/{id}       | Get a specific user              |
| POST   | /users            | Create a new user                |
| PUT    | /users/{id}       | Update a user                    |
| DELETE | /users/{id}       | Delete a user                    |
| GET    | /users/{id}/posts | Get all posts by a specific user |

##### Request/Response

1. Get User Details

Request

```http
GET /users/1 HTTP/1.1
Host: api.example.com
```

Response

```json
200 OK

{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "created_at": "2024-02-22T12:00:00Z"
}
```

2. Update User (PATCH Instead of PUT)

   Instead of sending the full object, a RESTful API supports partial updates
   using `PATCH`.

   Request

   ```http
   PATCH /users/1 HTTP/1.1
   Content-Type: application/json

   {
     "email": "alice_new@example.com"
   }
   ```

   Response

   ```json
   200 OK

   {
     "id": 1,
     "name": "Alice",
     "email": "alice_new@example.com"
   }
   ```

## HTTP Methods

HTTP methods are used to perform operations on the server. The most common
methods are:

- `GET`: Retrieve data from the server.
- `POST`: Create new data on the server.
- `PUT`: Update data on the server.
- `DELETE`: Remove data from the server.
- `PATCH`: Partially update data on the server.

## Status Codes

HTTP status codes are used to indicate the result of an HTTP request. Some
common status codes are:

- `200 OK`: The request was successful.
- `201 Created`: The request was successful, and a new resource was created.
- `400 Bad Request`: The request was invalid.
- `401 Unauthorized`: The request requires user authentication.
- `404 Not Found`: The requested resource was not found.
- `500 Internal Server Error`: The server encountered an error.
- `503 Service Unavailable`: The server is currently unavailable.
- `504 Gateway Timeout`: The server timed out while waiting for a response.
- `429 Too Many Requests`: The client has sent too many requests in a given
  amount of time.

## Usage: Real-World Examples

Base URL: `https://api.example.com/users`

### GET (Retrieve resources)

Used to fetch data without modifying it.

1. Get all users

   Request

   ```http
   GET /users HTTP/1.1
   Host: api.example.com
   ```

   Response

   ```json
   [
     {
       "id": 1,
       "name": "Alice",
       "email": "alice@example.com"
     },
     {
       "id": 2,
       "name": "Bob",
       "email": "bob@example.com"
     }
   ]
   ```

2. Get a single user by ID

   Request

   ```http
   GET /users/1 HTTP/1.1
   Host: api.example.com
   ```

   Response

   ```json
   {
     "id": 1,
     "name": "Alice",
     "email": "alice@example.com"
   }
   ```

### POST (Create a new resource)

Used to add new data to the server.

1. Create a new user

   Request

   ```http
   POST /users HTTP/1.1
   Content-Type: application/json

   {
     "name": "Charlie",
     "email": "charlie@example.com"
   }
   ```

   Response

   ```json
   201 Created

   {
     "id": 3,
     "name": "Charlie",
     "email": "charlie@example.com"
   }
   ```

### PUT (Update an existing resource)

Used to fully replace a resource.

1. Update a user (Full replacement)

   Request

   ```http
   PUT /users/1 HTTP/1.1
   Content-Type: application/json

   {
     "name": "Alice Johnson",
     "email": "alicejohnson@example.com"
   }
   ```

   Response

   ```json
   200 OK

   {
     "id": 1,
     "name": "Alice Johnson",
     "email": "alicejohnson@example.com"
   }
   ```

   The entire resource is replaced (both name and email must be sent, even if
   only one is changing).

### PATCH (Partially update an existing resource)

Used to partially modify a resource.

1. Update only the email of a user

   Request

   ```http
   PATCH /users/1 HTTP/1.1
   Content-Type: application/json

   {
     "email": "alice_new@example.com"
   }
   ```

   Response

   ```json
   {
     "id": 1,
     "name": "Alice",
     "email": "alice_new@example.com"
   }
   ```

   Only the email field is updated, not the entire user object.

### DELETE (Remove a resource)

Used to delete data from the server.

1. Delete a user

   Request

   ```http
   DELETE /users/1 HTTP/1.1
   Host: api.example.com
   ```

   Response

   ```json
   204 No Content
   ```

   The server responds with `204 No Content`, meaning the resource was
   successfully deleted.

### Summary of HTTP Methods

| Method | Purpose               | Idempotent | Example Endpoint         |
| ------ | --------------------- | ---------- | ------------------------ |
| GET    | Retrieve data         | Yes        | `/users` & `/users/{id}` |
| POST   | Create new data       | No         | `/users`                 |
| PUT    | Update data           | Yes        | `/users/{id}`            |
| PATCH  | Partially update data | No         | `/users/{id}`            |
| DELETE | Remove data           | Yes        | `/users/{id}`            |

### What is Idempotency?

Idempotency means that making the same request multiple times will result in the
same outcome.

#### Why is POST Not Idempotent?

- Every time you send a POST request, it creates a new resource with a new ID.

##### Example

Request

```http
POST /users
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

Response

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

Sending the same request again will create another user with a new ID:

Response

```json
{
  "id": 2,
  "name": "Alice",
  "email": "alice@example.com"
}
```

Since multiple identical POST requests create duplicate entries, POST is not
idempotent.

#### Why is PUT Idempotent?

Sending the same `PUT` request multiple times will overwrite the resource with
the same data.

##### Example

Request

```http
PUT /users/1
Content-Type: application/json

{
  "name": "Alice Johnson",
  "email": "alicejohnson@example.com"
}
```

Response

```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alicejohnson@example.com"
}
```

Sending the same request again will update the same user with the same data:

Response

```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alicejohnson@example.com"
}
```

The user remains the same. No new data is created. And since repeating the
request does not change the final result, PUT is idempotent.

#### Why is PATCH Not Idempotent?

Since `PATCH` updates only specific fields, sending the same request multiple
times may cause different results, depending on how the API processes it.

##### Example

Request

```http
PATCH /users/1
Content-Type: application/json

{
  "email": "alice_new@example.com"
}
```

Response

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice_new@example.com"
}
```

Second request changes another field:

Request

```http
PATCH /users/1
Content-Type: application/json

{
  "email": "alice_updated@example.com"
}
```

Response

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice_updated@example.com"
}
```

Since different requests can lead to different results over time, `PATCH` is not
idempotent.
