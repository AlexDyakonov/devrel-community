from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .services import get_path_upload_avatar, validate_size_image
from django.db import models
from backend import settings

# Create your models here.
class User(AbstractUser):
    middle_name     = models.CharField(max_length=100, blank=True, null=True)
    bio             = models.TextField(max_length=2000, blank=True, null=True)
    avatar          = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image]
    )
    sex             = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    birth_date      = models.DateField('Дата рождения', null=True, blank=True)

    # Обязательные поля
    first_name      = models.CharField(max_length=30, blank=False)
    last_name       = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.username

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roles   = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username