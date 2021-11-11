from typing import Text
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Scraping
# importar o token csrf
from django.views.decorators.csrf import csrf_protect

# Create your views here.

# generate code


def getCode():
    from datetime import datetime
    dataHora = datetime.now()
    code = str(dataHora.year)
    code += str(dataHora.month)
    code += str(dataHora.day)
    code += str(dataHora.hour)
    code += str(dataHora.minute)
    code += str(dataHora.second)
    code = str(int(round(int(code)/2, 0)))
    return code


# get all Scrapings
def showAll(request):

    s = Scraping.objects.filter()

    return render(request, 'scrapings.html', {
        'data': s,
    })

# get Scraping


def show(request, id):

    s = Scraping.objects.get(id=id)

    return render(request, 'scraping.html', {
        'data': [s],
    })

# new Scraping


def new(request):

    s = Scraping.objects.filter()

    return render(request, 'ScrapingNew.html', {
        'data': s,
    })

# salve new Scraping
# method post use csrf


@csrf_protect
def salve(request):
    code = getCode()
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    data_analyzer_nlp1 = request.POST.get("data_analyzer_nlp1")
    data_analyzer_nlp2 = request.POST.get("data_analyzer_nlp2")
    data_analyzer_nlp3 = request.POST.get("data_analyzer_nlp3")
    data_analyzer_nlp4 = request.POST.get("data_analyzer_nlp4")
    data_analyzer_nlp5 = request.POST.get("data_analyzer_nlp5")

    sp = Scraping(
        code=code,
        question=question,
        answer=answer,
        data_analyzer_nlp1=data_analyzer_nlp1,
        data_analyzer_nlp2=data_analyzer_nlp2,
        data_analyzer_nlp3=data_analyzer_nlp3,
        data_analyzer_nlp4=data_analyzer_nlp4,
        data_analyzer_nlp5=data_analyzer_nlp5,
    )

    sp.save()

    s = Scraping.objects.filter()

    return render(request, 'scrapings.html', {
        'data': s,
    })

# delete Scraping


def delete(request, id):

    id = int(id)

    Scraping.objects.filter(id=id).delete()

    s = Scraping.objects.filter()

    return render(request, 'scrapings.html', {
        'data': s,
    })


# Web Scraping
def scraping(question):

    if question:
        # NLP here
        question = question.strip()
        question = question.replace(' ', '_')
        # scraping target
        # 'https://pt.wikipedia.org/wiki/
        response = requests.get('https://pt.wikipedia.org/wiki/'+question)
        site = BeautifulSoup(response.text, 'html.parser')

        # identification of a standard class in the html that contains the fetched data
        temp = site.find('div', attrs={'id': 'noarticletext'})

        if temp:
            for s in temp.stripped_strings:
                # message for when the required data does not exist and or the search did not return anything
                if 'A Wikipédia não possui um artigo com este nome exato'.lower() in s.lower():
                    # response = requests.get('https://pt.wikipedia.org/w/index.php?search=   &ns0=1')
                    return {
                        'id': 0,
                        'text': 'Sem Resultados.',
                        'tag': '</>'
                    }

        # new identification of a standard class in the html that contains the fetched data
        temp = site.find('div', attrs={'class': 'mw-parser-output'})

        if temp:
            # through a regular expression, searching only the data between the <p></p> tags
            import re
            temp = temp.find_all(re.compile("^p"))

            data = list()
            # entering data into a list
            i = 0
            for item in temp:
                data.append({
                    'id': i+1,
                    'text': item.text,
                    'tag': item
                })
                i += 1

            return data

    return {
        'id': 0,
        'text': 'Sem Resultados.',
        'tag': '</>'
    }

# get data


def start(request):

    question = "Como cozinhar bananas"

    return render(request, 'scrapings.html', {
        'data': scraping(question),
    })
