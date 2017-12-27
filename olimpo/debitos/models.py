from django.db import models
from entidades.models import Entidade

# Create your models here.
class Debitos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(max_length=30)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)
    Entidade = models.ForeignKey(Entidade)
    def __str__(self):
        return self.descricao