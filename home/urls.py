from django.urls import path
from .views import home, chatbot

urlpatterns = [
    path('', home),
    path('chatbot/', chatbot)
]
