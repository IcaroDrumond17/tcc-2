from django.db import models

# Create your models here.
class Question(models.Model):
    code = models.CharField(max_length=15) #identificador gerado externamente
    code_relation = models.CharField(max_length=15) # relacionar a pergunta com a anterior
    question = models.CharField(max_length=500) #pergunta
    answer = models.CharField(max_length=500) #resposta

    #retorno
    def __str__(self):
        return self.question