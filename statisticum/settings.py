# -*- encoding: UTF-8 -*-
# Django settings for places project.
from __future__ import absolute_import
import os,logging
from django.utils.translation import ugettext_lazy as trans
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# HOSTS
DEFAULT_HOST = '127.0.0.1'
DB_HOST = os.getenv('DB_HOST', DEFAULT_HOST)
REDIS_HOST = os.getenv('REDIS_HOST', DEFAULT_HOST)
ALLOWED_HOSTS = ['*']

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


ADMINS = (
    ('Administrator', 'admin@statisticum.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'statisticum',              # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': DB_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': 3306,                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOGIN_URL = "/"
LOGIN_ERROR_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

USE_TZ = True 
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://www.statisticum.com/static/'
HOME_URL = 'http://www.statisticum.com/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#$49+_p6#x7g3zw3=@xr)=bq)i9qof##r1-7)u5%il-ya=yf&('
#if DEBUG:
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',      
]
#else:
    #TEMPLATE_LOADERS = [
    #    ('django.template.loaders.cached.Loader',(
    #        'django.template.loaders.filesystem.Loader',
    #        'django.template.loaders.app_directories.Loader',
    #    )),
    #]

DEFAULT_LOCALE_ENCODING='utf-8'
DEFAULT_CHARSET='utf-8'

LANGUAGES = (
    ('en', trans('English')),
    ('bg', trans(u'Български')),
)

MIDDLEWARE_CLASSES = (
    #'django_hosts.middleware.HostsMiddleware',
    #'autoload.middleware.AutoloadMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'statisticum.urls'
DEFAULT_HOST = 'default'
SESSION_COOKIE_DOMAIN = ".statisticum.com"

DEFAULT_TEMPLATE_DIR =  os.path.join(SITE_ROOT, "templates")

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DEFAULT_TEMPLATE_DIR, 
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
	'django.core.context_processors.i18n',
)



LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'locale'), )

INSTALLED_APPS = (
	#'redis_cache',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'statisticum.common',
    'statisticum.games',
    'bootstrapform',
    'registration'
)


AUTHENTICATION_BACKENDS = (
    #'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING_FILE = "statisticum.log"
if LOGGING_FILE:
    import logging
    loglevel = logging.DEBUG if DEBUG else logging.INFO
    logging.basicConfig(
        level=loglevel,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y%m%d %H%M%S',
        filename=LOGGING_FILE,
        filemode='a'
    )

FORCE_SCRIPT_NAME = ""

GLOBAL_MEDIA_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

MEDIA_GENERATORS = (
    'mediagenerator.generators.bundles.Bundles',
    'mediagenerator.generators.manifest.Manifest',
)
#'http://www.statisticum.com:1000/'


MEDIA_DEV_MODE = True
PRODUCTION_MEDIA_URL = STATIC_URL
DEV_MEDIA_URL = STATIC_URL


###################################################################

ACCOUNT_ACTIVATION_DAYS = 2
ACCOUNT_ACTIVATION_SEND = False
AUTH_PROFILE_MODULE = 'statisticum.common.UserProfile'

#CACHES = {
#    'default': {
#        'BACKEND': 'redis_cache.RedisCache',
#        'LOCATION': REDIS_HOST + ':6379',
#    }
#}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = REDIS_HOST
SESSION_REDIS_PORT = 6379
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'