# Django ToDo Application

## 📋 Project Overview

A complete Django-based ToDo application with full CRUD functionality, user authentication, and task management system.

---

## 🏗️ Project Structure

```
django_basic/
├── env/                          # Python Virtual Environment
├── ToDo/                         # Main Application Directory
│   ├── templates/                # HTML Templates Directory
│   │   ├── edit_task.html        # Edit Task Interface
│   │   ├── home.html             # Main Dashboard
│   │   ├── login.html            # User Login Page
│   │   └── register.html         # User Registration Page
│   ├── __pycache__/              # Python Bytecode Cache
│   ├── migrations/               # Database Migrations
│   ├── __init__.py               # Package Initialization
│   ├── admin.py                  # Admin Panel Configuration
│   ├── apps.py                   # App Configuration
│   ├── models.py                 # Database Models
│   ├── tests.py                  # Test Cases
│   ├── urls.py                   # App URL Routes
│   └── views.py                  # App Views
├── todo_main/                    # Project Configuration
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py                   # ASGI Configuration
│   ├── settings.py               # Project Settings
│   ├── urls.py                   # Main URL Routing
│   ├── views.py                  # Project Views
│   └── wsgi.py                   # WSGI Configuration
├── db.sqlite3                    # SQLite Database
└── manage.py                     # Django Management Script
```

---

## 🚀 Features

### ✅ Core Features

* User Registration
* Login and Logout
* Secure Authentication
* Create Tasks
* Edit Tasks
* Delete Tasks
* Mark Tasks Complete/Incomplete
* User Specific Task Lists

### 🎯 Advanced Features

* Task Filtering
* Search Tasks
* Responsive UI
* Real-time Updates

---

## 🛠️ Technology Stack

### Backend

* Python 3.x
* Django 4.x
* SQLite Database
* Django ORM

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Tools

* VS Code
* Git
* Virtual Environment

---

## 📦 Installation Guide

### Prerequisites

* Python 3.8+
* pip
* Git

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd django_basic
```

### Step 2: Create Virtual Environment

```bash
python -m venv env
```

### Step 3: Activate Environment

#### Windows

```bash
env\Scripts\activate
```

#### macOS / Linux

```bash
source env/bin/activate
```

### Step 4: Install Django

```bash
pip install django
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 7: Run Server

```bash
python manage.py runserver
```

### Step 8: Open Browser

```
http://127.0.0.1:8000/
```

---

## 📁 File Descriptions

### Configuration Files

* `manage.py` – Django command utility
* `settings.py` – Project configuration
* `urls.py` – URL routing
* `wsgi.py` – Deployment config
* `asgi.py` – Async config

### Application Files

* `models.py` – Database models
* `views.py` – Application logic
* `urls.py` – App routing
* `admin.py` – Admin panel
* `tests.py` – Unit tests

### Templates

* `home.html` – Dashboard
* `login.html` – Login page
* `register.html` – Register page
* `edit_task.html` – Edit task

---

## 🔧 Usage Guide

### Create Task

1. Login
2. Open Dashboard
3. Add New Task
4. Save

### Manage Task

* Edit Task
* Delete Task
* Mark Complete

### User

* Register Account
* Login
* Logout

---

## 🧪 Testing

```bash
python manage.py test ToDo
```

---

## 🔒 Security

* Password Hashing
* CSRF Protection
* ORM Security
* Session Authentication

---

## 🌐 Deployment

* Set DEBUG = False
* Configure Database
* Collect Static
* Use Gunicorn/Nginx

---

## 🤝 Contributing

1. Fork
2. Create Branch
3. Commit
4. Push
5. Pull Request


##Screenshots
<img width="960" height="571" alt="image" src="https://github.com/user-attachments/assets/086e936b-76c6-4ae8-a846-a2a50a8a6bba" />
<img width="960" height="570" alt="image" src="https://github.com/user-attachments/assets/7a22c0d5-477b-4607-8963-96743f104d06" />
<img width="957" height="574" alt="image" src="https://github.com/user-attachments/assets/bf084ce9-dbbd-4857-a2fb-dd3c0ca360e4" />
<img width="960" height="572" alt="image" src="https://github.com/user-attachments/assets/b3d66017-1ddc-44ac-96d7-4acebf479f79" />


