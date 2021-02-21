from django.db import models

# Create your models here.

class Messages(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    verification = models.CharField(max_length=255)
    message = models.TextField()
    verified = models.BooleanField()
    visible = models.BooleanField(default=True)
