from django.db import models

# Create your models here.


class dict(models.Model):
    ar = models.CharField(max_length=120)
    eng = models.CharField(max_length=120)