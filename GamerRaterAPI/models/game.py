from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.TextField()
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    estimated_time = models.IntegerField()
    age = models.IntegerField()
    overall_rating = models.IntegerField()