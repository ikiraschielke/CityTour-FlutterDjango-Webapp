from django.urls import path, include
from .views import *

#webapp paths, so that urls can get defined in city/urls.py
urlpatterns = [
    path('', include('city.urls')),
]
