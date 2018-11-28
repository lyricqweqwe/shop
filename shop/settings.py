import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))


SECRET_KEY = 'w)mypfm!i1_lvigm@rmb96v9rjly@%@i83bjm&l%t)o3+e#bz!'

DEBUG = True

ALLOWED_HOSTS = []


#第三方apps
EXT_APPS=[
    'bootstrap3'
]
#自己模块
MY_APPS=[
    'apps.home',
    'apps.detail',
    'apps.cate',
    'apps.search',
]
#系统apps
SYS_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS = EXT_APPS+MY_APPS+SYS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER':'root',
        'PASSWORD':'root',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 开启django时区 一般为false
USE_TZ = False

STATIC_URL = '/static/'
#配置静态文件整理根目录
# STATIC_ROOT = 'static_root'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

#配置访问多媒体的目录
MEDIA_URL = '/media/'
#配置文件上传的目录
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#==================邮箱配置===============

#发送邮件服务器地址
EMAIL_HOST ="smtp.163.com"

#发送邮件端口
EMAIL_PORT = 25

#发送邮件名字
EMAIL_HOST_USER = '13821671776@163.com'

# 授权码
EMIAL_HOST_PASSWORD = '9191'

#是否启用tls安全协议
EMAIL_USE_TLS = True

# ========== 缓存的配置=========
# pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://127.0.0.1/3",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
}

# ========SESSION 缓存配置======
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# session失效的时间 7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒

