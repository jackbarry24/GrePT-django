from django.core.management import call_command
import os
import django
import sys
from django.conf import settings


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
        ALLOWED_HOSTS=['127.0.0.1'],
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
    else:
        call_command('runserver')

if __name__ == '__main__':
    main()
    

