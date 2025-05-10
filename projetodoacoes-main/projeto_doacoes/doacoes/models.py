from django.db import models

class Doacao(models.Model):
    nome_doador = models.CharField(max_length=100)
    email_doador = models.EmailField()
    data_doacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.nome_doador} - {self.descricao[:30]}"
