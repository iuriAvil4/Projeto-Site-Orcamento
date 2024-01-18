from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
