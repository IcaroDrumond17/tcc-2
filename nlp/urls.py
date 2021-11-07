from django.urls import path
from .views import input

urlpatterns = [
    path('input/<str:question>/', input)
]
