# testai/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('testai/tests/v1/execute', views.execute_test, name='execute_test'),
]
