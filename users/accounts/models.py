from django.db import models
from django.utils import timezone

class Account(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150,default='')
    lastname = models.CharField(max_length=150,default='')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
