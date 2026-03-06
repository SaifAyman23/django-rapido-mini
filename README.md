# Django Rapido MINI V1.0

A lightweight, production-ready Django project template designed for quick project setup. This is the simplified version of the comprehensive Django Rapido template - perfect for smaller projects that don't need all the bells and whistles.

## Features

- **Django 5.2** - Latest Django framework
- **Django REST Framework** - Build REST APIs quickly
- **Unfold Admin** - Modern, beautiful Django admin interface
- **SQLite by default** - Ready to use out of the box (PostgreSQL supported)
- **Docker Support** - Containerize your application easily
- **API Documentation** - Auto-generated with DRF Spectacular
- **CORS Enabled** - Ready for frontend integration
- **User Authentication** - Token-based auth with custom user model

## Quick Start

### Prerequisites

- Python 3.10+
- Windows, macOS, or Linux

### Installation

1. **Clone the project**
   ```bash
   git clone <your-repo-url>
   cd django-rapido-mini
   ```

2. **Initialize the project** (one command does everything!)
   ```bash
   make init
   ```

   This will:
   - Create `.env` from `.env.example`
   - Generate a secure `SECRET_KEY`
   - Run database migrations
   - Create a superuser
   - Collect static files

3. **Start the development server**
   ```bash
   make run
   ```

4. **Visit the sites**
   - Admin: http://localhost:8000/admin
   - API Docs: http://localhost:8000/api/docs/
   - API: http://localhost:8000/api/

### Default Credentials

After running `make init`, log in with:
- **Username:** `admin`
- **Password:** `admin123`

Change these in `.env` via `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD`.

## Available Commands

| Command | Description |
|---------|-------------|
| `make install` | Install Python dependencies |
| `make init` | Initialize project (env, secret key, migrations, superuser) |
| `make run` | Start development server |
| `make migrate` | Run database migrations |
| `make makemigrations` | Create new migrations |
| `make shell` | Open Django shell |
| `make createsuperuser` | Create a new superuser |
| `make collectstatic` | Collect static files |
| `make clean` | Remove Python cache files |
| `make docker-up` | Start Docker services |
| `make docker-down` | Stop Docker services |

## Project Structure

```
django-rapido-mini/
├── accounts/              # User authentication app
│   ├── models.py         # Custom user model
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   └── urls.py           # URL routing
├── common/               # Shared utilities
│   ├── admin.py          # Custom admin configuration
│   ├── models.py         # Base models
│   ├── views.py          # Base views
│   ├── pagination.py     # Custom pagination
│   └── ...
├── project/              # Django project settings
│   ├── settings/
│   │   ├── base.py       # Base settings
│   │   ├── local.py      # Local development
│   │   ├── production.py # Production settings
│   │   └── testing.py    # Testing settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── guides/              # Documentation guides
├── .env.example         # Environment variables template
├── .env                 # Your environment variables
├── requirements.txt     # Python dependencies
├── Makefile             # Project commands
├── Dockerfile           # Docker configuration
└── docker-compose.yml   # Docker Compose configuration
```

## Database Configuration

### SQLite (Default - Ready to Use)

The project uses SQLite by default, which requires no additional setup:
```python
# project/settings/base.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### PostgreSQL (Production Recommended)

To switch to PostgreSQL, edit `.env`:
```env
# .env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=project_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Then uncomment the PostgreSQL section in `project/settings/base.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME", "project_db"),
        "USER": os.getenv("DB_USER", "project_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password123"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
```

**Note:** PostgreSQL requires `psycopg` which is already in requirements.txt.

## Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
# Django Settings
DJANGO_ENVIRONMENT=local
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL - optional)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=project_db
DB_USER=project_user
DB_PASSWORD=password123
DB_HOST=localhost
DB_PORT=5432

# Admin Superuser
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123

# API Documentation
API_TITLE=My API
API_DESCRIPTION=My Django REST API
API_VERSION=1.0.0
```

## Docker Deployment

### Quick Start with Docker

1. **Build and run**
   ```bash
   make docker-up
   ```

2. **Access the application**
   - Django: http://localhost:8000
   - Admin: http://localhost:8000/admin

3. **Stop services**
   ```bash
   make docker-down
   ```

### Manual Docker Commands

```bash
# Build images
make docker-build

# View logs
make docker-logs

# Run migrations in container
make docker-migrate

# Create superuser in container
make docker-createsuperuser

# Shell into container
make docker-shell

# Clean up (remove containers and volumes)
make docker-clean
```

## API Authentication

The template uses Token-based authentication:

1. **Get Token**
   ```
   POST /api/auth/token/
   Body: {"username": "admin", "password": "admin123"}
   ```

2. **Use Token**
   ```
   Authorization: Token your-token-here
   ```

## Admin Interface

Access the admin at `/admin` with Unfold - a modern Django admin theme:
- Sleek, modern UI
- Dark mode support
- Enhanced filtering and search

## Guides

Check the `guides/` directory for detailed documentation:

- **Settings Guide** - Database, email, security settings
- **Models Guide** - Creating and managing models
- **Serializers Guide** - DRF serializer patterns
- **Views Guide** - API view best practices
- **Permissions Guide** - Access control
- **Filters Guide** - Filtering and searching
- **Pagination Guide** - Custom pagination
- **Middleware Guide** - Request/response middleware
- **Exceptions Guide** - Custom exception handling
- **Unfold Admin Guide** - Admin customization

## Customization

### Adding New Apps

```bash
py manage.py startapp myapp
```

### Creating Models

Edit `myapp/models.py`:
```python
from django.db import models
from common.models import TimestampedModel

class MyModel(TimestampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table = 'my_model'
    
    def __str__(self):
        return self.name
```

### Creating API Endpoints

1. Create serializer in `myapp/serializers.py`
2. Create view in `myapp/views.py`
3. Add URLs in `myapp/urls.py`
4. Include in main `project/urls.py`

## Development Workflow

```bash
# Full setup
make install
make init

# Daily development
make run

# After model changes
make makemigrations
make migrate

# Create superuser
make createsuperuser

# Clean cache
make clean
```

## Troubleshooting

### Migration Errors
```bash
# Reset migrations (development only)
make db-reset
```

### Static Files Not Loading
```bash
make collectstatic
```

### Permission Denied (Linux/Mac)
```bash
chmod +x manage.py
```

## What's Included

### Python Packages
- Django 5.2
- Django REST Framework
- django-cors-headers
- django-filter
- drf-spectacular (API docs)
- django-unfold (admin theme)
- psycopg (PostgreSQL)
- whitenoise (static files)
- gunicorn (production server)

### Ready-to-Use
- Custom user model
- Token authentication
- REST API endpoints
- Admin interface
- API documentation
- Docker configuration

## Differences from Django Rapido (Full Version)

This is the **MINI** version. The full version includes:
- Celery for async tasks
- Redis integration
- Email backend
- More comprehensive testing
- Additional middleware
- Extended guides

Use this mini version for:
- Quick prototypes
- Simple projects
- Learning Django
- Small to medium applications

## License

MIT License - Use freely for your projects.

## Support

For issues and questions, please refer to the guides in `guides/` or check Django documentation at https://docs.djangoproject.com/
