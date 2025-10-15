# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    nombre_temporal = models.CharField(max_length=255)
    ruta = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    tamano = models.IntegerField()
    descripcion_corta = models.CharField(max_length=150, blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    descargas = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'archivo'


class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    created = models.DateTimeField()
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    contenido = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    fk_estatu = models.ForeignKey('Estatu', models.DO_NOTHING)
    fk_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comentario'


class Estatu(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estatu'


class Publicacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    resumen = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    vistas = models.IntegerField(blank=True, null=True)
    fk_categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    fk_estatu = models.ForeignKey(Estatu, models.DO_NOTHING)
    fk_foto_portada = models.ForeignKey(Archivo, models.DO_NOTHING)
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publicacion'


class PublicacionArchivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    fk_archivo = models.ForeignKey(Archivo, models.DO_NOTHING)
    fk_publicacion = models.ForeignKey(Publicacion, models.DO_NOTHING)
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publicacion_archivo'
        unique_together = (('fk_publicacion', 'fk_archivo'),)
