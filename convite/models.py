from django.db import models

class ConfirmacaoPresenca(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=20,
        choices=[("presencial", "Presencial"), ("online", "Online")]
    )
    data_confirmacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.tipo}"
