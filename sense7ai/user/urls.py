from django.urls import include,path
from user import api
from django.conf.urls.static import static
import os
from django.conf import settings

urlpatterns = [
    path('api/users', api.users_api.as_view(), name='users')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)