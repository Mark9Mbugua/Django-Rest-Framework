from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(max_length=100)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name + ',' + self.location
