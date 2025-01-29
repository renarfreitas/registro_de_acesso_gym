#from .models import Colaborador, ColetaFaces, Treinamento
from django.contrib import admin
from registro.models import (
    Colaborador, ColetaFaces, Treinamento)

class ColetaFacesInline(admin.StackedInline):
    model = ColetaFaces
    extra = 0

class ColaboradorAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = (ColetaFacesInline,)

admin.site.register(Colaborador, ColaboradorAdmin)

# admin.site.register(Colaborador)
# admin.site.register(ColetaFaces)
admin.site.register(Treinamento)