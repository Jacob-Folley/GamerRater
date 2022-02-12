from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.CharField(max_length=55)