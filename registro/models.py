from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from random import randint

class Colaborador(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    foto = models.ImageField(upload_to='foto/')
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        seq = self.nome + '_COLAB' + str(randint(10000000, 9999999))
        self.slug = slugify(seq)
        super().save(*args, **kwargs)
    
class ColetaFaces(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='colaborador_coletas')
    image = models.ImageField(upload_to='roi/')



class Treinamento(models.Model):
    modelo = models.FileField(upload_to='treinamento/')

    class Meta:
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'

    
    def __str__(self):
        return 'Classificadores (frontalface)'
    
    def clean(self):
        model = self.__class__
        if model.objects.exclude(id=self.id).exists():
            raise ValidationError('Só pode haver um arquivo salvo.')