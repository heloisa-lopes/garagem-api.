from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.descricao} - {self.id}"