from django.urls import path
from .views import *

urlpatterns = [
    path('users/',author, name='author'),
]