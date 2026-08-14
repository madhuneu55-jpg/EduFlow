# EduFlow

EduFlow is a Django-based educational discussion platform where users can create and participate in discussion rooms, communicate with other users, and manage their profiles.

## Features

- User registration and login
- User authentication
- Create, update and delete discussion rooms
- Search rooms
- Topic-based discussions
- Room messaging
- Participant management
- Activity feed
- User profiles
- REST API
- JWT authentication
- Protected API endpoints
- CRUD operations

## Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- HTML
- CSS
- SQLite
- Git & GitHub


## Project Structure

```text
EduFlow/
│
├── Studybud/                    # Django project configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── base/                        # Main EduFlow application
│   ├── api/                     # REST API
│   │   ├── serializers.py       # API serializers
│   │   ├── urls.py              # API URLs
│   │   └── views.py             # API views
│   │
│   ├── migrations/              # Database migrations
│   ├── templates/base/          # App templates
│   ├── models.py                # Database models
│   ├── views.py                 # Web views
│   ├── forms.py                 # Django forms
│   └── urls.py                  # App URLs
│
├── static/                      # CSS and static files
│
├── templates/                   # Shared templates
│
├── manage.py                    # Django management utility
├── requirements.txt             # Python dependencies
├── .gitignore                   # Files ignored by Git
└── README.md                    # Project documentation