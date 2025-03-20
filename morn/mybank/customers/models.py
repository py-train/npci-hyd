from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    acnum = models.IntegerField(primary_key=True)
    balance = models.FloatField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f'Customer({self.name})'
