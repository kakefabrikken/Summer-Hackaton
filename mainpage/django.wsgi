import os
import sys
 
sys.path.append('/var/www/mainpage')
sys.path.append('/var/www/mainpage/mainpage')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mainpage.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
