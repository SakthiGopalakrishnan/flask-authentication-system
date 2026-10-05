# Flask Authentication System

A full-featured authentication and user management web application built using Flask and SQLAlchemy.

## Features

### Authentication
- User Registration
- User Login
- User Logout
- Password Hashing using Werkzeug
- Forgot Password
- Password Reset

### Profile Management
- View Profile
- Edit Username
- Change Password
- Upload Profile Image
- Delete Account

### Admin Dashboard
- View All Users
- Search Users
- Pagination
- Promote User to Admin
- Demote Admin to User
- Delete Users

### Security
- Session-Based Authentication
- Role-Based Authorization (Admin/User)
- Environment Variables (.env)
- Custom Error Pages (404, 403, 500)

### Database
- SQLAlchemy ORM
- SQLite Database
- CRUD Operations
- User Roles
- Profile Images

### Flask Features
- Blueprints
- Templates (Jinja2)
- Flash Messages
- Decorators
- File Uploads

## Project Structure

```text
Flask-Authentication-System

routes/
│
├── auth.py
├── profile.py
└── admin.py

templates/
static/

app.py
models.py
services.py
decorators.py
requirements.txt
```

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- Bootstrap
- Jinja2
- Werkzeug
- Flask-WTF
- python-dotenv

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project

```bash
cd Flask-Authentication-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```text
SECRET_KEY=your_secret_key
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Learning Concepts Implemented

- Flask Routing
- Templates and Jinja2
- Sessions
- Authentication
- Authorization
- Password Hashing
- SQLAlchemy ORM
- CRUD Operations
- Search and Pagination
- Blueprints
- Decorators
- Environment Variables
- Error Handlers
- File Uploads


## Author

Sakthi G
