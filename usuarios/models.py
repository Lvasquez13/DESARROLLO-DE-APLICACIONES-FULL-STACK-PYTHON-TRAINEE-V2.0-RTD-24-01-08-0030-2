from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # puedes agregar campos extra si quieres
    telefono = models.CharField(max_length=20, blank=True)