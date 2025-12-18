from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title