# Create your models here.
from django.db import models

class Transliteration(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # image = models.FilePathField(path="/img")

    def __str__(self):
        return str(self.pk) + " - Transliteration"