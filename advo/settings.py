"""
Django settings for advo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, base64

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "iwdq=bgnj2tsp*uc2(_kd59!0724wrkf(@m9$g0^7rds)jgruj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Jenny Gao', 'technology@theharvardadvocate.com'),
    ('Yuqi Hou', 'hou@college.harvard.edu'),
    ('Luciano Arango', 'lucianoarango@college.harvard.edu'),
    ('Alex Sedlack', 'asedlack@college.harvard.edu'),
    ('Diane Yang', 'dianeyang@college.harvard.edu')
)

MANAGERS = ADMINS

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sammysignal@gmail.com'
EMAIL_HOST_PASSWORD = base64.b64decode('eXVsaXR0bGU=')
DEFAULT_FROM_EMAIL = 'sammysignal@gmail.com'

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'tinymce',
    'ajax_select',
    'south',
    'magazine',
    'blog',
    'payments',
    'django_social_share',
    'contacts',
    'redactor',
    'select2',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'advo.urls'

WSGI_APPLICATION = 'advo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    #http://stackoverflow.com/questions/3756841/django-media-url-blank
    'django.core.context_processors.media',
    'magazine.context_processors.search_typeahead',
)

AJAX_LOOKUP_CHANNELS = {
     'contributor' : ('magazine.lookups', 'ContributorLookup'),
     'tag' : ('magazine.lookups', 'TagLookup'),
}

STRIPE_BUY_PUBLIC_KEY = os.environ.get("STRIPE_BUY_PUBLIC_KEY", "pk_test_7mkjcG8fQj3qmdhCgP92Pq4g")
STRIPE_DONATE_PUBLIC_KEY = os.environ.get("STRIPE_DONATE_PUBLIC_KEY", "pk_test_66u2FQCcD717Ot7UGj1IvEsN")

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'paste_retain_style_properties': "color font-size",
    'content_css': "/static/magazine/css/tinymce_custom.css",
    'theme': "advanced",
    'cleanup_on_startup': False,
    'custom_undo_redo_levels': 10,
}
# Setting up logs
# http://ianalexandr.com/blog/getting-started-with-django-logging-in-5-minutes.html
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': 'advocatemain.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'WARNING',
#         },
#         'magazine': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#         },
#         'payments': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#         },
#     }
# }

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

try:
    from local_settings import *
except ImportError:
    pass

try:
    from search_settings import *
except ImportError:
    pass




import django
from django.conf import settings
from django.core.mail import send_mail
