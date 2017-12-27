from django.db import models

# Create your models here.
class Entidade(models.Model):
    Descrição = models.CharField(max_length=100)
    