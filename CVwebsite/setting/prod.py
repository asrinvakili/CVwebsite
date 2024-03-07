from CVwebsite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8sxmvqyf2iwf^fbuyu3f6-c9ham_38^t1@yh#p2&^u7^qv8x&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['asrin-vakili.ir', 'www.asrin-vakili.ir']

SITE_ID = 1

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

