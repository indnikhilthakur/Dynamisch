from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class register_poc_main(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = PhoneNumberField()
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.first_name +" "+ self.email

# this signal creates auth token for users
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender = settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance = None, created = False, **kwrgs):
#     if created:
#         Token.objects.create(user=instance)