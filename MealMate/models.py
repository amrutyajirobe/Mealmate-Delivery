from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return str(self.name)
