from django.contrib import admin
from core.models import Categoria, Estatu, Archivo, Publicacion, PublicacionArchivo, Comentario

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'createdat', 'updatedat', 'fk_user']
    
admin.site.register(Categoria, CategoriaAdmin)

class EstatuAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'createdat', 'updatedat', 'fk_user']
    
admin.site.register(Estatu, EstatuAdmin)

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'createdat', 'updatedat', 'fk_user']
    
admin.site.register(Archivo, ArchivoAdmin)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'resumen', 'contenido','created', 'updated', 'vistas', 'fk_categoria','fk_estatu','fk_foto_portada','fk_user']
    
admin.site.register(Publicacion, PublicacionAdmin)

class PublicacionArchivoAdmin(admin.ModelAdmin):
    list_display = ['id','created', 'updated','fk_archivo','fk_publicacion','fk_user']

admin.site.register(PublicacionArchivo,PublicacionArchivoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id','contenido', 'created', 'updated','fk_user','fk_estatu','fk_publicacion']

admin.site.register(Comentario,ComentarioAdmin)