from django.shortcuts import render
#from questions.models import Question
from typing import List
# importar o token csrf
from django.views.decorators.csrf import csrf_protect
# recurso json para emitir respostas no formato json
from django.http import JsonResponse
#from unidecode import unidecode

# Create your views here.


def input(request, code_before, question):

    lista = list()
    lista.append({
        'code_current': 0,
        'code_before': code_before,
        'question': question,
        'input': question,
        'output': 'Desculpe, mas não sei informar.'
    })

    return JsonResponse(lista, safe=False)
