from django.db import models

# Create your models here.


class Tasks(models.Model):
    content = models.TextField()
