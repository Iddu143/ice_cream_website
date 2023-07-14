from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add more fields as needed

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

def __str__(self):
    return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

