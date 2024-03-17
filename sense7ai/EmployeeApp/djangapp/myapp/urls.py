from . import views
from django.urls import path
urlpatterns=[
    path('', views.empreg,name='empreg'),
    path('update/',views.update,name='update'),
    path('index/',views.index,name='index'),
]