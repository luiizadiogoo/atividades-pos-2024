from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()

    def __str__(self):
        return self.nome

class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    segundos = models.IntegerField()

    def __str__(self):
        return self.nome
