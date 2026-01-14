from django.db import models


# Create your models here.
class User(models.Model):
    username = (models.CharField(max_length=20),)
    password = (models.CharField(max_length=20),)
    pfp = (models.ImageField(blank=True),)
    dateOfRegistration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
