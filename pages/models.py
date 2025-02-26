from django.db import models

# Create your models here.
from django.db import models

class Convocacao(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='convocacoes/')
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=255)


    def __str__(self):
        return self.titulo

class postagem(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='postagem/')
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=255)


    def __str__(self):
        return self.titulo