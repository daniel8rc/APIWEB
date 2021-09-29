from rest_framework import routers
from django.urls import (re_path, path)
from .api import Api

app_name = 'football'

urlpatterns = [
    path('football-yesterday', Api.as_view(), name='football-yesterday')
]