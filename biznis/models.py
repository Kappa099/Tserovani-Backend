from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # e.g. fruit stand, butcher
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name