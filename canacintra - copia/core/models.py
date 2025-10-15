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
