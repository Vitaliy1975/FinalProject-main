from django.db import models

# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="", unique=True)
    description = models.CharField(max_length=255, default="", blank=True, null=True)
