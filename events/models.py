from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    information = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=200)
    date = models.DateField()

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    member_list = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="events_joined",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
