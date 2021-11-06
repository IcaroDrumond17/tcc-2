from django.urls import path
from .views import showAll, show, new, salve, delete, start

urlpatterns = [
    path('todas/', showAll),
    path('analise/<int:id>/', show),
    path('analise-novo/', new),
    path('analise-novo-salvar/', salve),
    path('analise-remover/<int:id>/', delete),
    path('', start),
]
