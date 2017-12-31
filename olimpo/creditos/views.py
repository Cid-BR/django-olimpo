from django.shortcuts import render
from django.views.generic import ListView
from olimpo.creditos.models import Creditos

# Create your views here.
class CreditosList(ListView):
    model = Creditos