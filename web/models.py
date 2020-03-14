from django.conf import settings
from django.db import models
from django.utils import timezone


class Site(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    status = models.IntegerField(default=200)
    priority = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
