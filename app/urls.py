# messages/urls.py
from django.urls import path
from .views import MessageAPI

urlpatterns = [
    path('api/messages/', MessageAPI.as_view()),
]