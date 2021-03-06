# Django settings for munkiwebadmin project.

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x@hgx4r!1rm@c4lax96tx88*d1v+m$&)w1ur4-xvcqj(8as_$q'

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
    # our apps
    'catalogs',
    'pkgsinfo',
    'manifests',
    'process',
    # Uncomment the next line if you've installed django_wsgiserver
    # and want to serve this Django app using it
    # 'django_wsgiserver',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'munkiwebadmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'munkiwebadmin/templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

WSGI_APPLICATION = 'munkiwebadmin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# using sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#### end basic Django settings

# needed by django-wsgiserver when using staticserve=collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'munkiwebadmin/collected_static')
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'munkiwebadmin/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# django ldap auth
USE_LDAP = False
# LDAP authentication support
if USE_LDAP:
    import ldap
    from django_auth_ldap.config import LDAPSearch, PosixGroupType
    
    # LDAP settings
    AUTH_LDAP_SERVER_URI = "ldap://foo.example.com"
    AUTH_LDAP_BIND_DN = ""
    AUTH_LDAP_BIND_PASSWORD = ""
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        "ou=People,o=ExampleCorp,c=US",
        ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        "ou=Groups,o=ExampleCorp,c=US",
        ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")
    AUTH_LDAP_GROUP_TYPE = PosixGroupType()
    AUTH_LDAP_FIND_GROUP_PERMS = True
    AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", 
                               "last_name": "sn",
                               "email": "mail"}
    # Cache group memberships for an hour to minimize LDAP traffic
    AUTH_LDAP_CACHE_GROUPS = True
    AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600


if USE_LDAP:
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

# https://docs.djangoproject.com/en/1.9/ref/settings/#login-url
LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/manifests/'

# who gets code error notifcations when DEBUG is False
# https://docs.djangoproject.com/en/1.9/ref/settings/#admins
ADMINS = (
     ('Local Admin', 'root@example.com'),
)
# who gets broken link notifcations when DEBUG is False
# https://docs.djangoproject.com/en/1.9/ref/settings/#managers
MANAGERS = ADMINS

###########################################################################
# munkiwebadmin-specific
###########################################################################

# APPNAME is user-visible web app name
APPNAME = 'MunkiWebAdmin2'
# MUNKI_REPO_DIR holds the local filesystem path to the Munki repo
MUNKI_REPO_DIR = '/munki_repo'
#MUNKI_REPO_DIR = '/Volumes/repo'

# path to the makecatalogs binary
MAKECATALOGS_PATH = '/munki-tools/code/client/makecatalogs'

# provide the path to the git binary if you want MunkiWebAdmin to add and commit
# manifest edits to a git repo
# if GITPATH is undefined or None MunkiWebAdmin will not attempt to do a git add
# or commit
#GIT_PATH = '/usr/bin/git'
