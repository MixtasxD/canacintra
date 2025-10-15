from django.db import models

from django.contrib.auth.models import User 

# Create your models here.
class Categoria(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=60)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(null=True, blank=True)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)

    class Meta:
        managed = True 
        db_table = 'categoria'
        verbose_name_plural= 'Categoria'


class Estatu(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=60)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(null=True, blank=True)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)

    class Meta:
        managed = True 
        db_table = 'estatu'
        verbose_name_plural= 'Estatu'


class Archivo(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=255)
    nombre_temporal = models.CharField(max_length=255)
    ruta = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    tamano = models.IntegerField()
    descripcion_corta = models.CharField(max_length=150, blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    descargas = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(null=True, blank=True)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)

    class Meta:
        managed = True
        db_table = 'archivo'
        verbose_name_plural = 'Archivo'


class Publicacion(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo = models.CharField(max_length=255)
    resumen = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(null=True, blank=True)
    vistas = models.IntegerField(blank=True, null=True)
    fk_categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    fk_estatu = models.ForeignKey(Estatu, models.DO_NOTHING)
    fk_foto_portada = models.ForeignKey(Archivo, models.DO_NOTHING)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)

    class Meta:
        managed = True
        db_table = 'publicacion'
        verbose_name_plural = 'Publicacion'


class PublicacionArchivo(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True,
    serialize=False, verbose_name='ID')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    fk_archivo = models.ForeignKey(Archivo, models.DO_NOTHING)
    fk_publicacion = models.ForeignKey(Publicacion, models.DO_NOTHING)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'publicacion_archivo'
        verbose_name_plural = 'Publicacion_archivo'
        unique_together = (('fk_publicacion', 'fk_archivo'),)


class Comentario(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True,
    serialize=False, verbose_name='ID')
    contenido = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    fk_estatu = models.ForeignKey('Estatu', models.DO_NOTHING)
    fk_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'comentario'
        verbose_name_plural = 'Comentario'



