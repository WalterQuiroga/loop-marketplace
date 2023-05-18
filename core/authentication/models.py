from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):


    username = models.CharField(max_length=50, unique = True, null=False)
    email = models.EmailField(max_length=130, unique = True , null = False)
    phone_numer = models.CharField(max_length=13, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password'] 

    def __str__(self):
        return f"{self.username} - {self.email}"
    