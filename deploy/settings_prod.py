# turn off debugging in production
DEBUG = False

# settings for the production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'djangousr',
        'PASSWORD': 'gq6877',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# allowed hosts for our production site
ALLOWED_HOSTS = ['162.243.159.92']

STATIC_ROOT = '/opt/mec_env/static/'
MEDIA_ROOT = '/opt/mec_env/media/'
