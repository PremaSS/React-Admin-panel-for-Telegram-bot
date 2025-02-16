"""
WSGI config for admin_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.contrib.auth.hashers import make_password
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_project.settings')

application = get_wsgi_application()
password = '123'  # замените на ваш желаемый пароль
hashed_password = make_password(password)
print(hashed_password)
