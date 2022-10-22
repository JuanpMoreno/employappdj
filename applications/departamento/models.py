from email.policy import default
from enum import unique
from operator import mod
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    shor_name = models.CharField('Nombre corto', max_length = 20)
    anulate = models.BooleanField('Anulado', default = False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique.together = ('name','shor_name')

    def __str__(self) -> str:
        return str(self.id) + '-' + self.name + '-' + self.shor_name