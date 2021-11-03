from django.shortcuts import render
from .models import Question
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


# get all questions
def showAll(request):

    q = Question.objects.filter()
 
    return render(request, 'questions.html', {
        'data': q,
    })

# get question
def show(request, id):

    q = Question.objects.get(id=id)

    return render(request, 'questions.html', {
        'data': [q],
    })

# new question
def new(request):

    q = Question.objects.filter()

    return render(request, 'questionNew.html', {
        'data': q,
    })

# salve new question
# method post use csrf
@csrf_protect
def salve(request):
    code = getCode()
    code_relation = request.POST.get("code_relation")
    question = request.POST.get("question")
    answer = request.POST.get("answer")

    q = Question(
        code=code,
        code_relation=code_relation,
        question=question,
        answer=answer
    )

    q.save()

    q = Question.objects.filter()
 
    return render(request, 'questions.html', {
        'data': q,
    })

# edit question
def edit(request, id):

    items = q = Question.objects.filter();
    q = Question.objects.get(id=id)

    return render(request, 'questionEdit.html', {
        'data': q,
        'items': items
    })

# update question
# method post use csrf
@csrf_protect
def update(request):

    id = int(request.POST.get("id"))
    code_relation = request.POST.get("code_relation")
    question = request.POST.get("question")
    answer = request.POST.get("answer")

    Question.objects.filter(id=id).update(
        code_relation=code_relation,
        question=question,
        answer=answer
    )

    q = Question.objects.filter()
 
    return render(request, 'questions.html', {
        'data': q,
    })

# remove question
def remove(request, id):

    items = Question.objects.filter()
    q = Question.objects.get(id=id)

    return render(request, 'questionRemove.html', {
        'items': items,
        'data': q
    })

# delete question
# method post use csrf
@csrf_protect
def delete(request):

    id = int(request.POST.get("id"))

    Question.objects.filter(id=id).delete()

    q = Question.objects.filter()
 
    return render(request, 'questions.html', {
        'data': q,
    })