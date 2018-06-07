from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField()
    email = models.EmailField()
    