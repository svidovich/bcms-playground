from django.db import models


class Verb(models.Model):
    infinitive = models.CharField(max_length=64, blank=False, null=False, unique=True)
    english = models.CharField(max_length=64, blank=False, null=False, unique=True)
