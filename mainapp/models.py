from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

