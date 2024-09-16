# Social-Networking-App
Certainly! Here's a structured **README.md** file for your social networking API project:

---

# Social Networking Application API

This project is a RESTful API for a social networking application built using Django and Django REST Framework. The API includes functionalities like user signup, login, searching users, sending/accepting/rejecting friend requests, listing friends, rate-limiting, and more.

## Features

- **User Signup & Login**: Users can sign up and log in using their email and password.
- **Search Users**: Users can search for others by name or email (case-insensitive, paginated results).
- **Friend Requests**: Users can send, accept, or reject friend requests.
- **Friend List**: List friends who have accepted the request.
- **Pending Requests**: View pending friend requests.
- **Rate Limiting**: Users cannot send more than 3 friend requests per minute.

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite (can be swapped with any database of choice)
- **Testing**: pytest
- **Containerization**: Docker

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd socialNetworkingApp
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run migrations to set up the initial database schema:

```bash
python manage.py migrate
```

### 5. Create Superuser

Create an admin account for accessing the Django admin panel:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000`.

---

## API Endpoints

### 1. User Signup and Login

- **Signup**: `POST /api/signup/`
- **Login**: `POST /api/login/`

### 2. Search Users

- **Search**: `GET /api/users/search/?query=<keyword>`  
  Returns up to 10 users per page that match the search query by name or email.

### 3. Friend Requests

- **Send Request**: `POST /api/friends/request/`
- **Accept Request**: `POST /api/friends/accept/`
- **Reject Request**: `POST /api/friends/reject/`

### 4. Friend Lists and Pending Requests

- **Friends List**: `GET /api/friends/list/`
- **Pending Requests**: `GET /api/friends/pending/`

---

## Running Tests

### 1. Running Unit Tests

Run the tests using `pytest`:

```bash
pytest
```

### 2. Test Coverage

You can check the test coverage with:

```bash
pytest --cov
```

## Conclusion

This API provides the core functionalities of a social networking platform, including user management, friend requests, and user searches. Additional features can be built on top of this foundation for a complete social networking application.

---

## Developer Notes

- Ensure all required environment variables are set, especially the `DJANGO_SETTINGS_MODULE` for proper settings configuration.
- SQLite is used by default. For production, swap out the database to Postgres or MySQL as needed.
- Rate limiting is implemented to prevent users from sending too many friend requests in a short period.

---

Let me know if you need any additional details or adjustments for this README!
