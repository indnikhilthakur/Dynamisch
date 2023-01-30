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



from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class register_user(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_no = PhoneNumberField()
    first_name = models.CharField(max_length=100, blank=True, null =True)
    last_name = models.CharField(max_length=100, blank=True, null =True)
    address = models.CharField(max_length=200, blank=True, null=True)
    token = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return self.email +" "+self.first_name


class user_kyc_info(models.Model):
    def name_file(instance, filename):
        return '/'.join(['images', str(instance.kyc_img_name), filename]) 
    kyc_email = models.ForeignKey(register_user, to_field="email", on_delete=models.CASCADE, null=True, blank = True)
    kyc_image = models.ImageField(null=True, blank=True, upload_to = name_file)
    kyc_img_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.kyc_img_name
