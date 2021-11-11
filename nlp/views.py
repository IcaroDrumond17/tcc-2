from django.shortcuts import render
from questions.models import Question
from scraping.models import Scraping
from typing import List
# importar o token csrf
from django.views.decorators.csrf import csrf_protect
# recurso json para emitir respostas no formato json
from django.http import JsonResponse
from unidecode import unidecode
import spacy
import nltk
import re  # expressoes regulares

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


#nltk
def stemization(text):

    tokenizador = nltk.WhitespaceTokenizer()
    radical = nltk.RSLPStemmer()

    tokenized_text = tokenizador.tokenize(text)

    items = []

    for p in tokenized_text:
        items.append(radical.stem(p))
    
    return ' '.join(items)


def textFormated(text):

     # question received
    text = unidecode(text)
    text = text.lower()
    text = text.replace('?', '')
    text = text.replace(',', '')
    text = text.strip()

    text = internetLanguage(text)

    # verb tenses
    return stemization(text)


def nlpSpacy(question):
    # ADJ - adjetivo
    # CCONJ - Conjunção
    # DET - Determinar
    # NOUN - Substantivo
    # PRON - Pronome
    # ADV - Adverbio
    # VERB - Verbo
    # ADP - Adposição
    # NUM - Numero
    # DAT - Data
    # interjeição
    # PUNC - Pontuação
    # PROPN -nome proprio
    nlp = spacy.load("pt_core_news_sm") 
    question = nlp(question)

    for i in question:
        print("-> "+i.text+" -> "+i.pos_)

    return 0


def input(request, question):

    # remove caracters %20
    question = question.replace('%20', ' ')

    print("=========================")
    print(question)
    nlpSpacy(question)
    print("=========================")

    # lowercase
    question = question.lower()

    # get questions in database
    q = Question.objects.filter()

    # inserted list
    result = list()
    


    # web scraping here
    if len(q) <= 0:
        result.append({
            'code_current': 0,
            'question': question,
            'input': question,
            'output': 'É hora de usar o web scraping...'
        })
    else:
        for a in q:
            result.append({
                'code_current': a.code,
                'question': a.question,
                'input': question,
                'output': a.answer
            })

    # question received
    question_received = textFormated(question)

    i = 0
    controller = False
    # compare questions and return answers
    for b in result:
        i += 1
        # question found
        question_found = textFormated(b['question'])

        if question_found == question_received:
            controller = True
            break

    templist = list()

    l = 0
    for c in result:
        l += 1
        if i == l and controller == True:
            templist.append(c)
            break

    if len(templist) <= 0:
        templist.append({
            'code_current': 0,
            'question': question,
            'input': question,
            'output': 'É hora de usar o web scraping...'
        })

    result = templist

    return JsonResponse(result, safe=False)


# tokenização
def tokenizador():

    return []
