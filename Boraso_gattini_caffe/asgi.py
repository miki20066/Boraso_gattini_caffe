import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boraso_gattini_caffe.settings')

application = get_asgi_application()