from django.shortcuts import render
from questions.models import Question
from typing import List
# importar o token csrf
from django.views.decorators.csrf import csrf_protect
# recurso json para emitir respostas no formato json
from django.http import JsonResponse
from unidecode import unidecode

# Create your views here.

# NPL


def internetLanguage(item):
    item = item.replace('vc', 'voce')
    item = item.replace('vcs', 'voces')
    item = item.replace('eh', 'e')
    item = item.replace('tb', 'tambem')
    item = item.replace('tbm', 'tambem')
    item = item.replace('oq', 'o que')
    item = item.replace('dq', 'de que')
    item = item.replace('td', 'tudo')
    item = item.replace('pq', 'por que')

    return item


def verbTenses(verb, n):

    # tokenize
    verb = verb.split(' ')

    # remove the last 3 words to standardize verb tenses
    temp = list()
    for x in verb:
        if len(x) > 3:
            # remove the last 3 words
            temp.append(x[0:len(x)-n])
        else:
            temp.append(x)

    # destokenize
    return ' '.join(temp)

def textFormated(text):

    text = internetLanguage(text)

    # question received
    text = unidecode(text)
    text = text.lower()
    text = text.replace('?', '')
    text = text.strip()

    # verb tenses
    return verbTenses(text, 3)

def input(request, code_before, question):

    # remove caracters %20
    question = question.replace('%20', ' ')
    # lowercase
    question = question.lower()

    # get questions in database
    q = Question.objects.filter()

    #inserted list
    result = list()
    
    # web scraping here
    if len(q) <= 0:
        result.append({
            'code_current': 0,
            'code_before': code_before,
            'question': question,
            'input': question,
            'output': 'É hora de usar o web scraping...'
        })
    else:
        for x in q:
            result.append({
                'code_current': x.code,
                'code_before': code_before,
                'question': x.question,
                'input': question,
                'output': x.answer
            })

    # question received
    question_received = textFormated(question)

    equals = 0
    code = ''

    # compare questions and return answers
    for x in result:
        # question found
        question_found = textFormated(x['question'])

        qrList = question_received.split(' ')
        qfList = question_found.split(' ')

        amount = 0
        # find questions received with found
        for l in qrList:
            # compare
            if l in qfList:
                amount += 1
        
        if amount >= equals:
            equals = amount
            code = x['code_current']

    templist = list()

    for x in result:
        if code == x['code_current']:
            templist.append(x)
            break

    result = templist

    return JsonResponse(result, safe=False)
