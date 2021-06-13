'''Use this for production'''

from .base import *

SECRET_KEY = "SECRET_KEY443rwfsf3w43434defsfw33fsdf43r"

DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATICFILES_LOCATION = "static"
# STATICFILES_STORAGE = "config.storages.StaticStorage"
STATIC_URL = "/static/"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# MEDIAFILES_LOCATION = "media"
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"
# SECURE_LOCATION = "secure"
# SECURE_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, SECURE_LOCATION)
