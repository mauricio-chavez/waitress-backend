"""Development settings."""

from .base import *  # NOQA
from .base import env

from datetime import timedelta


# Base
DEBUG = env.bool('DJANGO_DEBUG', True)

# Security
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='4ra7dxard(&tmw$b5s9--akuakuisreal0v4!!f_-h7i)b_96aw'
)

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Development apps
INSTALLED_APPS += [
    'django_extensions',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = APPS_DIR / 'media'

# Security
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

# Admin
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')

# JWT tokens
GRAPHQL_JWT['JWT_EXPIRATION_DELTA'] = timedelta(days=1)