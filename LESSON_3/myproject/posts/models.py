from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)


# max_length=75 => tamanho máximo da string
# auto_now_add=True => adiciona uma data automaticamente
