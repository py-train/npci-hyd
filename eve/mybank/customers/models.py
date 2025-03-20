from django.db import models

# Create your models here.
class Customer(models.Model):
    sex_choices = {
        'M': 'Male',
        'F': 'Female'
    }
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=10, choices=sex_choices)