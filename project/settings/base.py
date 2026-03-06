import os
from pathlib import Path
from .unfold_config import *
from dotenv import load_dotenv
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

# Determine which environment we're in
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'local')

# Load environment variables
load_dotenv('.env')

if ENVIRONMENT == 'production':
    load_dotenv('.env.production', override=True)
else:
    load_dotenv('.env.local', override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY - keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-&r+5c(o9pqlj@6h$&r%4+8&=ab!u0=z3mj#9$r=%^h4jz(*ukg")

# Debug mode (overridden by environment-specific settings)
DEBUG = os.getenv("DEBUG", "True") == "True"

# Allowed hosts (overridden by environment-specific settings)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

INSTALLED_APPS = [
    # Unfold admin (before django.contrib.admin)
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.inlines",
    
    # Local apps
    "accounts",
    "common",
    "dashboard",
    
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Third-party
    'corsheaders',
    "rest_framework",
    "django_filters",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # For static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

"""
Database configuration.
PostgreSQL setup with connection pooling.
"""

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
#         "NAME": os.getenv("DB_NAME", "project_db"),
#         "USER": os.getenv("DB_USER", "project_user"),
#         "PASSWORD": os.getenv("DB_PASSWORD", "password123"),
#         "HOST": os.getenv("DB_HOST", "localhost"),
#         "PORT": os.getenv("DB_PORT", "5432"),
#         "CONN_MAX_AGE": 600,
#         "OPTIONS": {
#             "connect_timeout": 10,
#         }
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Testing configuration
TESTING = os.getenv("TESTING", "False") == "True"
if TESTING:
    DATABASES["default"]["NAME"] = os.getenv("TEST_DATABASE_NAME", "project_test_db")


# Legacy login credentials (consider removing if not needed)
LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "s@gmail.com")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "1")

# URL Configuration
ROOT_URLCONF = "project.urls"
WSGI_APPLICATION = "project.wsgi.application"

# Custom user model
AUTH_USER_MODEL = "common.CustomUser"

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# https://docs.djangoproject.com/en/5.1/ref/settings/#date-input-formats
DATE_INPUT_FORMATS = [
    "%d.%m.%Y",  # Custom input
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
]

# https://docs.djangoproject.com/en/5.1/ref/settings/#datetime-input-formats
DATETIME_INPUT_FORMATS = [
    "%d.%m.%Y %H:%M:%S",  # Custom input
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
]


# Internationalization
LANGUAGE_CODE = "en"

LANGUAGES = (
    ("ar", _("العربية")),
    ("en", _("English")),
)

USE_TZ = True
TIME_ZONE = "UTC"
I18N = True
USE_I18N = True
USE_L10N = True  # Localized formatting (numbers, dates, etc.)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
    # os.path.join(BASE_DIR, 'apps', 'accounts', 'locale'),
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "dashboard/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'dashboard.context_processors.dashboard_context',
            ],
        },
    },
]

# Static & Media files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-app-password")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "noreply@localhost.com")

"""
============================================================================================
REST Framework settings.
API documentation configuration (DRF Spectacular).
============================================================================================
"""

# REST Framework (DRF 3.16)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_PAGINATION_CLASS": "common.pagination.StandardPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/hour",
        "user": "1000/hour",
    },
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    'DATE_FORMAT': '%d.%m.%Y',  # Output format for dates
    'DATETIME_FORMAT': '%d.%m.%Y %H:%M:%S',  # Output format for datetimes
    'TIME_FORMAT': '%H:%M:%S',
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,  # Input formats
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS,
}


# DRF Spectacular Settings
SPECTACULAR_SETTINGS = {
    "TITLE": os.getenv("API_TITLE", "Rapido Mini API"),
    "DESCRIPTION": os.getenv("API_DESCRIPTION", "Modern Django REST API with latest technologies"),
    "VERSION": os.getenv("API_VERSION", "1.0.0"),
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
    "SERVERS": [
        {"url": "http://localhost:8000", "description": "Local development server"},
        {"url": os.getenv("PRODUCTION_URL", "https://api.example.com"), "description": "Production server"},
    ],
    "SCHEMA_PATH_PREFIX": "/api/v[0-9]/",
    
    # Security configuration for TokenAuthentication
    "SECURITY": [
        {
            "TokenAuth": [],
        }
    ],
    "COMPONENTS": {
        "securitySchemes": {
            "TokenAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                "description": """
                Token-based authentication.
                
                **Format**: `Token <your_token>`
                
                **Example**: `Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`
                
                To obtain a token, POST to `/api/auth/token/` with your username and password.
                """
            }
        },
        # Optional: Add a schema for token responses
        "schemas": {
            "Token": {
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "description": "Authentication token",
                        "example": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
                    }
                }
            }
        }
    },
    
    # Swagger UI customization
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,
        "displayOperationId": True,
        "tryItOutEnabled": True,
        "filter": True,
    },
    
    # Additional settings
    "TAGS": [
        {"name": "auth", "description": "Authentication endpoints"},
        {"name": "users", "description": "User management"},
        {"name": "core", "description": "Core API functionality"},
    ],
}


"""
Security settings - CORS, SSL, CSRF, etc.
Base security settings (overridden by environment-specific settings).
"""

# CORS Configuration
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(",")
CORS_TRUSTED_ORIGINS = os.getenv("CORS_TRUSTED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(",")

# Security Settings (defaults - overridden in production.py)
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False") == "True"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "False") == "True"
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "0"))

SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}

# CSRF_FAILURE_VIEW = "common.views.csrf_failure"

# Admin User Configuration (for initial setup)
DJANGO_SUPERUSER_USERNAME = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
DJANGO_SUPERUSER_EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
DJANGO_SUPERUSER_PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")


"""
Logging configuration.
Console and file handlers with rotation.
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "maxBytes": 1024 * 1024 * 10,  # 10MB
            "backupCount": 5,
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": os.getenv("LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": os.getenv("LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "celery": {
            "handlers": ["console", "file"],
            "level": os.getenv("LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

# Create logs directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


# ===========================
# Docker Configuration
# ===========================
DOCKER_ENVIRONMENT = os.getenv("DOCKER_ENVIRONMENT", "local")

