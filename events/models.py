from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()

    host = models.CharField(max_length=200)
    members = models.CharField(max_length=200)

    def __str__(self):
        return self.title
