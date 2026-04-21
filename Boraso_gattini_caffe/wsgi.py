import os

from django.core.wsgi import get_wsgi_application

# Sostituito 'CREAZZO_GattiniCafe.settings' con il tuo nuovo nome
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boraso_gattini_caffe.settings')

application = get_wsgi_application()