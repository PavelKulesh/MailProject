from django.db import models


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    login = models.CharField('Login', max_length=50)
    password = models.CharField('Password', max_length=50)
