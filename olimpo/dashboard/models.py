from django.db import models

# Create your models here.

class Entradas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(max_length=30)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

class Saidas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(max_length=30)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)