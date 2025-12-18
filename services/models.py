from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
