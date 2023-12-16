from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from .services import get_path_upload_avatar, validate_size_image
from django.db import models
from backend import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Specialization(models.Model):
    name = models.CharField('Специализация', max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField('Навыки', max_length=100)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    GRADE_CHOICES = (
        ('intern', 'Intern'),
        ('apprentice', 'Apprentice'),
        ('junior', 'Junior Developer'),
        ('mid', 'Mid-level Developer'),
        ('senior', 'Senior Developer'),
        ('lead', 'Lead Developer'),
        ('principal', 'Principal Developer'),
        ('architect', 'Architect'),
        ('tech_lead', 'Tech Lead'),
        ('engineering_manager', 'Engineering Manager'),
        ('chief_architect', 'Chief Architect'),
    )

    username        = None
    email = models.EmailField('Почта', unique=True)
    first_name      = models.CharField('Имя', max_length=30, blank=True)
    last_name       = models.CharField('Фамилия', max_length=30, blank=True)
    middle_name     = models.CharField('Отчество', max_length=100, blank=True, null=True)
    phone_number    = models.CharField('Номер телефона', max_length=15, blank = True, null=True)
    city            = models.TextField('Город', max_length=2000, blank=True, null=True)
    sex             = models.CharField('Пол', max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    birth_date      = models.DateField('Дата рождения', null=True, blank=True)
    grade           = models.CharField('Ступень', max_length=20, choices=GRADE_CHOICES, blank=True)
    work_experience = models.PositiveIntegerField('Опыт работы (в годах)', default=0)
    is_devrel       = models.BooleanField('DevRel', default=False)
    specializations = models.ManyToManyField(Specialization, related_name='users', blank=True, verbose_name='Специализации')
    skills = models.ManyToManyField(Skill, related_name='users', blank=True, verbose_name='Навыки')


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
@receiver(post_save, sender=User)
def set_random_password(sender, instance : User, created, **kwargs):
    if created and not instance.is_superuser:
        password = User.objects.make_random_password()
        instance.set_password(password)
        instance.save(update_fields=['password'])