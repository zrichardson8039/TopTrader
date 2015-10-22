from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False # change this to false eventually

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

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
