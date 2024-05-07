"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# settings 모듈의 위치를 mysite/wsgi.py 파일에서 지정함
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# 개발용 runserver는 실행 옵션으로도 지정 가능함
# $ python manage.py runserver --settings=mysite.settings
application = get_wsgi_application()
