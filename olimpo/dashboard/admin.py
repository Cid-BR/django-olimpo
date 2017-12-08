from django.contrib import admin
from olimpo.dashboard.models import Entradas, Saidas

# Register your models here.


@admin.register(Entradas)
class EntradasAdmin(admin.ModelAdmin):
    list_display = ('descricao','data', 'valor')

@admin.register(Saidas)
class SaidasAdmin(admin.ModelAdmin):
    list_display = ('descricao','data', 'valor')
