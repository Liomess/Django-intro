from django.db import models

# Create your models here.

# Normal class
class Student:
    id:int
    name: str



# class converted to DB

class Feature (models. Model):
    name = models. CharField(max_length=100)
    details = models. CharField(max_length=500)

#  by using models.Model ...it creates a by default attribute which is 'id' to the specified db.