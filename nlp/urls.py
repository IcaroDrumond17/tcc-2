from django.urls import path
from .views import input

urlpatterns = [
    path('input/<int:code_before>/<str:question>/', input)
]
