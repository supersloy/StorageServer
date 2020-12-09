"""
Django settings for MapStorageServer project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from os import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('APP_SECRET', 'change-me')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = environ.get('API_ALLOWED_HOSTS').split(';')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django REST framework 
    'rest_framework',
    # Request manager
    'requesthandler.apps.RequesthandlerConfig',
    # CORS
    'corsheaders',
    #'gridfs_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MapStorageServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MapStorageServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': environ.get("POSTGRES_DB", "metadata"),
        'ENGINE': 'django.db.backends.postgresql',
        'USER': environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': environ.get("POSTGRES_PASSWORD", "password"),
        'HOST': environ.get("POSTGRES_DB_HOST", "localhost"),
        'PORT': environ.get("POSTGRES_DB_PORT", 5432),
    },
    'filestorage': {
        'NAME': environ.get("POSTGRES_DB", "metadata"),
        'ENGINE': 'django.db.backends.postgresql',
        'USER': environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': environ.get("POSTGRES_PASSWORD", "password"),
        'HOST': environ.get("POSTGRES_DB_HOST", "localhost"),
        'PORT': environ.get("POSTGRES_DB_PORT", 5432),
    },
    'metadata': {
        'NAME': environ.get("POSTGRES_DB", "metadata"),
        'ENGINE': 'django.db.backends.postgresql',
        'USER': environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': environ.get("POSTGRES_PASSWORD", "password"),
        'HOST': environ.get("POSTGRES_DB_HOST", "localhost"),
        'PORT': environ.get("POSTGRES_DB_PORT", 5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CORS_ORIGIN_ALLOW_ALL = True

# # defaults to default local mongodb server
# DEFAULT_GRIDFS_URL = 'mongodb://127.0.0.1:27017'
# # if set to None, it will refuse to serve files and raise an Exception
# DEFAULT_GRIDFS_SERVE_URL = None
# DEFAULT_GRIDFS_COLLECTION = 'storage'
# DEFAULT_FILE_STORAGE = 'gridfs_storage.storage.GridFSStorage'

static_root = environ.get('API_STATIC_FILES', 'srv/static')
os.makedirs(static_root, mode=0o755, exist_ok=True)
STATIC_ROOT = static_root
# STATICFILES_DIRS = [
#     BASE_DIR / 'common-static',
# ]
STATIC_URL = '/static/'
