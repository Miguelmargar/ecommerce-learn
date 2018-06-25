from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-2a1_0&#(q3a0$w_drb46)9vtso_l$lfx_nh3@ugj-b$%o0fuw'

ALLOWED_HOSTS = ['ecomerce-miguelmargar.c9users.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')