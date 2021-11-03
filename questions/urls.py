from django.urls import path
from .views import showAll, show, new, salve, edit, update, remove, delete

urlpatterns = [
    path('', showAll),
    path('pergunta/<int:id>/', show),
    path('pergunta-novo/', new),
    path('pergunta-novo-salvar/', salve),
    path('pergunta-editar/<int:id>', edit),
    path('pergunta-editar-salvar/', update),
    path('pergunta-remover/<int:id>/', remove),
    path('pergunta-remover-salvar/', delete)
]
