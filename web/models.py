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


class Row(models.Model):
    row_number = models.IntegerField()

    def __str__(self):
        return str(self.row_number)


class Log(models.Model):
    site = models.ForeignKey('web.Site', on_delete=models.CASCADE, related_name='logs')
    row = models.ForeignKey('web.Row', on_delete=models.CASCADE, related_name='logs')
    ip = models.CharField(max_length=200)
    click_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ip
