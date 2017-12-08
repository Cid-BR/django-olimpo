from django.shortcuts import render
from olimpo.dashboard.models import Entradas, Saidas
# Create your views here.
def home(request):
    total_ent = 0
    for ent in Entradas.objects.all():
        total_ent += ent.valor

    total_sai = 0
    for sai in Saidas.objects.all():
        total_sai += sai.valor

    context = dict(
        total_entradas = total_ent,
        total_saidas = total_sai,
        diferenca = (total_ent - total_sai)
    )

    return render(request, 'totais.html', context)