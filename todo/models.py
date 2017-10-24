from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField()


class Uploads(models.Model):
    name=models.CharField(max_length=200)
    ip = models.GenericIPAddressField(blank=True , null=True)
    file = models.ImageField(upload_to=u'photos', blank=True)