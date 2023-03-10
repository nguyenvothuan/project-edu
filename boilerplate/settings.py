"""
Django settings for boilerplate project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
import environ
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6%hc3+^4=3phyx=86dqp%kl!g850jsv1keaw4u7tv(b&k_d324'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = [
    # TODO: Move allowed origin, secret keys, database host, port, etc. to environment variables 
    # (instead of directly setting in this file) for easy configuring the project in other environments.
    
    # TODO: add cors allowed origin for the frontend. Currently, only allow the server to call itself.
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Application definition

# Keep this list ordered alphabetically.
INSTALLED_APPS = [
    'ckeditor',
    'coreapi',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'graphene_django',
    'rest_framework',
    'rest_framework_simplejwt',
    # Apps
    'accounts',
    'observers',
    'advisors',
    'companies',
    'job',
    'schools',
    'students',
    'recruiters',
]

MIDDLEWARE = [
    # 'log_request_id.middleware.RequestIDMiddleware',
    # Keep CORS middleware near the top as possible to apply it early and allow header manipulation
    # Check out https://github.com/adamchainz/django-cors-headers#setup
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boilerplate.urls'

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

WSGI_APPLICATION = 'boilerplate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.environ['POSTGRES_NAME'],
        # 'USER': os.environ['POSTGRES_USER'],
        # 'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        # 'HOST': 'localhost',
        # 'PORT': '5432',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # dont fucking set this. This is for authorization in django view, why we are using swagger ui.
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'COERCE_DECIMAL_TO_STRING': False,
}


LOGIN_EXEMPT_URLS = ["/api/v1.0/test_apps/register/",
                     "/api/v1.0/test_apps/login/"]
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# JWT_AUTH = {
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
#     'JWT_ALLOW_REFRESH': False,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#     'JWT_AUTH_HEADER_PREFIX': 'token',
# }

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# Configuration for Swagger
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    }
}

AUTH_USER_MODEL = 'accounts.User'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # 'request_id': {
        #     '()': 'log_request_id.filters.RequestIDFilter'
        # }
    },
    'formatters': {
        'standard': {
            # 'format': '%(request_id)s [%(message)s] %(asctime)s',
            'datefmt': '%d-%m-%Y %H:%M:%S'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'master_app.log'),
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
            # 'filters': ['request_id'],
        },

        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}


# GraphQL
GRAPHENE = {
    'SCHEMA': 'boilerplate.schema.schema'
}
