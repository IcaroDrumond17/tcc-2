from django.shortcuts import render
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
    code_relation = request.POST.get("code_relation")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    data_analyzer_nlp1 = request.POST.get("data_analyzer_nlp1")
    data_analyzer_nlp2 = request.POST.get("data_analyzer_nlp2")
    data_analyzer_nlp3 = request.POST.get("data_analyzer_nlp3")
    data_analyzer_nlp4 = request.POST.get("data_analyzer_nlp4")
    data_analyzer_nlp5 = request.POST.get("data_analyzer_nlp5")

    sp = Scraping(
        code=code,
        code_relation=code_relation,
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