from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def add_amount(self):
        self.amount += 1

    def subtract_amount(self):
        if self.amount > 0:
            self.amount -= 1