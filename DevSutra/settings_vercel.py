from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['.vercel.app', '.now.sh']

# Use SQLite for simplicity on Vercel
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3',
    }
}
