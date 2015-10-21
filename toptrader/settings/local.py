"""
Django settings for toptrader project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join, dirname, abspath
import getpass
from django.conf import global_settings


ADMINS = (
        ('Zach Richardson', 'zrichardson1114@gmail.com')

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'jtb-hl38nx9tejj)3sx%n))nob9&=t%7x&n4#t7ecwdinj=96h'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'toptrader_dev',
        'USER': 'toptrader_dev',
        'PASSWORD': 'toptrader_dev',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # TODO enable when have a sentry key
    # 'raven.contrib.django.raven_compat',
    'rest_framework',
    'apps.common',
    'apps.contests',
    'apps.stockmarket',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 50,
}

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

USE_TZ = True
TIME_ZONE = 'America/Denver'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (join(BASE_DIR, 'static', 'static_dirs'),)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'toptrader.urls'
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

WSGI_APPLICATION = 'toptrader.wsgi.application'

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'


#DJANGO REGISTRATION REDUX SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'