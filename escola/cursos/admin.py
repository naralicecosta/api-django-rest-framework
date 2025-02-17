#aqui fazemos o registro das models
from django.contrib import admin
from .models import Curso, Avaliacao

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'criacao', 'atualizacao', 'ativo']
    
@admin.register(Avaliacao)
class AvalicacaoAmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo']
