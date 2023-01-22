from django.db import models


# Create your models here.
class model_movies2(models.Model):
    movie = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.movie +" "+ self.character