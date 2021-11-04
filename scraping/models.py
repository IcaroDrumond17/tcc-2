from django.db import models

# Create your models here.
class Scraping(models.Model):
    code = models.CharField(max_length=15) #identificador gerado externamente
    question = models.CharField(max_length=500) #pergunta
    answer = models.CharField(max_length=500) #resposta
    data_analyzer_nlp1 = models.TextField() # dados analizados 1 // tempo de resposta
    data_analyzer_nlp2 = models.TextField() # dados analizados 2 // url pesquisada
    data_analyzer_nlp3 = models.TextField() # dados analizados 3 // 
    data_analyzer_nlp4 = models.TextField() # dados analizados 4 //
    data_analyzer_nlp5 = models.TextField() # dados analizados 5 //

    #criterio 0% 50% 100% repostas validas

    #retorno
    def __str__(self):
        return self.question
