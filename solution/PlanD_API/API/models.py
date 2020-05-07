from django.db import models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=10, blank=True, unique=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name