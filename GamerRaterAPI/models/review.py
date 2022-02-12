from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    review = models.CharField(max_length=55)