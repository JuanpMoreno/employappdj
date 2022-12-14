from distutils.command.upload import upload
from operator import mod
from random import choices
from tabnanny import verbose
from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length = 50)

    class Meta: 
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

JOB_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro'),
)

class Empleado(models.Model):
    first_name = models.CharField('Nombres', max_length = 60)
    last_name = models.CharField('Apellidos', max_length = 60)
    full_name = models.CharField('Nombres completos', max_length =120, blank=True)
    job = models.CharField('Trabajo', max_length = 50, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_de_vida = RichTextField()

    class Meta:
        verbose_name = 'Mis subditos'
        verbose_name_plural = 'Clase obrera'
        ordering = ['first_name']


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name