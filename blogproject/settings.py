"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'unn!knl%n46(^9q1ody(n+5=m2r693nek7aabd_7v%l+820_lq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',
    'haystack',
    'blog',
    'read_statistics',
    'comment',
    'likes',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# 配置静态文件路径,静态文件包括css,js,image
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
# nginx
STATIC_ROOT='/var/www/jzfBlog.top/static/'

CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'PIL'

# 自定义参数
EACH_RAGE_BLOG_NUMBER = 10

# ckeditor扩展
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': (
# 			['div','Source','-','Save','NewPage','Preview','-','Templates'],
# 			['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
# 			['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
# 			['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
# 			['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
# 			['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
# 			['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
# 			['Link','Unlink','Anchor'],
# 			['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
# 			['Styles','Format','Font','FontSize'],
# 			['TextColor','BGColor'],
# 			['Maximize','ShowBlocks','-','About', 'pbckcode'],
# 		),
#        'width':'auto',
#       'height': '180',
#        'tabSpaces': 4,
#        'removePlugins': 'elementsPath',
#        'resize_enabled': False,
# 	}
# }


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
        ),
    },

    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['TextColor', 'BGColor', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['Smiley', 'SpecialChar', 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# 缓存设置
CACHES = {
        'default':{
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

#自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
