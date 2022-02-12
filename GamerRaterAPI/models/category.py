from django.db import models

class Category(models.Model):
    type = models.TextField()