from django.db import models

# Create your models here.


class model_movies_api(models.Model):
    movie = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.movie +" "+ self.character

# this signal creates auth token for users
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwrgs):
    if created:
        Token.objects.create(user=instance)