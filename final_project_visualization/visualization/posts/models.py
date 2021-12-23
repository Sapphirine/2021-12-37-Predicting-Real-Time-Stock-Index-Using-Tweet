from django.db import models

class Post(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.start}"