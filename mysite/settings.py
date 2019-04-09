"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import shutil
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hv_4y40dd1j)5g+s(h466w4&hbgqznvlz_+o^a01#wqqm+)mdl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'homepage',
    'account',
    'catalog',
    'portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            'CONTENT_PROVIDERS': [
                {   'provider': 'django_mako_plus.JsContextProvider' },
                {   'provider': 'django_mako_plus.CompileScssProvider',
                    'sourcepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss'),
                    'targetpath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                },
                {   'provider': 'django_mako_plus.CssLinkProvider',
                    'filepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                },
                {   'provider': 'django_mako_plus.JsLinkProvider' },
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'intex2',
        'USER': 'postgres',
        'PASSWORD': 'imcd4017',
        'HOST': 'localhost',
        'PORT': '',
    }
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# A logger for DMP
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # SECURITY WARNING: never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'dmp_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'dmp_console':{
            'class':'logging.StreamHandler',
            'formatter': 'dmp_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['dmp_console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}