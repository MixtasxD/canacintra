from django.contrib import admin
from core.models import Categoria, Estatu

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'createdat', 'updatedat', 'fk_user']
    
admin.site.register(Categoria, CategoriaAdmin)

class EstatuAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'createdat', 'updatedat', 'fk_user']
    
admin.site.register(Estatu, EstatuAdmin)
