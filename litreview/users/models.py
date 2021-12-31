from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCIRBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR,'Createur'),
        (SUBSCIRBER, 'Abonné'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
