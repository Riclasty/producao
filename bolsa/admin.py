from django.contrib import admin
from bolsa import models
# Register your models here.



@admin.register(models.Familia)
class Familiaadm(admin.ModelAdmin):
        list_display = 'id', 'nome', 'nis', 

@admin.register(models.Pessoa)
class Pessoaadm(admin.ModelAdmin):
        list_display = 'id', 'nome', 'data_nascimento', 'altura', 'peso','vacina', 'gestante', 'pccu', 'data_preventivo'
