from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def chatbot(request):
    return render(request, 'chatbot.html')
