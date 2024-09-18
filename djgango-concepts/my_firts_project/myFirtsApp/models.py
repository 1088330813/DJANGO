from django.db import models

# Create your models here.

# The first model is a car
class Car(models.Model):
    title = models.TextField(max_length=250) # max of data receive