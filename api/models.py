from django.db import models
from uuid import uuid4

class Evento(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Participante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
