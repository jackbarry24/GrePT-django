from django.core.management import call_command
import os
import django
import sys
from django.conf import settings
from webapp.secret import DJANGO_SECRET_KEY


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

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

def boot_django():
    settings.configure(
        ROOT_URLCONF='webapp.urls',
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        SECRET_KEY=DJANGO_SECRET_KEY,
        ALLOWED_HOSTS=['127.0.0.1'],
        STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')],
        TEMPLATE_CONTEXT_PROCESSORS = [
            'django.core.context_processors.request',
        ],
        TEMPLATES=TEMPLATES,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3'
            }
        },
        INSTALLED_APPS = (
            'django.contrib.staticfiles',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.core.serializers.json',
            'webapp',
        ),
        TIME_ZONE = 'UTC',
        USE_TZ = True,
        STATIC_URL = '/static/',
    )
    django.setup()

def main():
    
    boot_django()
    if len(sys.argv) > 1 and sys.argv[1] == 'migrate':
        call_command('migrate')
    elif len(sys.argv) > 1 and sys.argv[1] == 'shell':
        call_command('shell')
    else:
        call_command('runserver')

if __name__ == '__main__':
    main()
    

