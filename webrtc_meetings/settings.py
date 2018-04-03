"""
Django settings for webrtc_meetings project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')3q*z-@97ql!1abn4#*0tezk4e_zxwbp&fq8)og1q)=*x0342a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cacheops',
    'django_rq',
    'django_rq_dashboard',
    'channels',
    'timezone_field',
    'service_access',
    'meeting_room',
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

ROOT_URLCONF = 'webrtc_meetings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webrtc_meetings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": ['redis://localhost:6379/10',],
        },
        "ROUTING": "webrtc_meetings.routing.channel_routing",
    },
}

CACHEOPS_REDIS = {
    'host': 'localhost', # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 2,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended

}

WEBSOCKET_BASE_URL = '/meetings/'

CACHE_REFRESH_DURATION = 10800
CACHEOPS = {
    'meeting_room.meeting': {'ops': 'all',  #refresh every 3 hrs
                             'timeout': CACHE_REFRESH_DURATION},
    'service_access.*': {'ops': 'all',
                         'timeout': CACHE_REFRESH_DURATION}, #refresh every 3 hrs
    'auth.user': {'ops': 'all',
                   'timeout': CACHE_REFRESH_DURATION},  #refresh every 3 hrs
}

RQ_QUEUES = {
    'default': {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0,
    'DEFAULT_TIMEOUT': 360,
    },
}

HTTP_AUTH_REALM = 'meeting-room'
WS_OFFLINE_NOTICE = 'OFFLINE'

ROOM_KEY_FORMAT = 'room-%(room_id)s'

ICE_SERVERS = [         # pls update with your ice credentials
  {
    'urls': 'stun:stun.l.google.com:19302',
  },
  {
    'urls': 'stun:202.153.34.169:8002?transport=tcp',
  },
  {
    'urls': 'turn:202.153.34.169:8002?transport=udp',
    'credential': 'dhanush123',
    'username': 'dhanush'
  },
];
