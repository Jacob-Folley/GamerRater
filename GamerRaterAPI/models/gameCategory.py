from django.db import models
from django.contrib.auth.models import User

class GameCategory(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    categoryId = models.ForeignKey("Category", on_delete=models.CASCADE)