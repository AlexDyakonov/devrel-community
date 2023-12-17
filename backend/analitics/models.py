from django.db import models
from users.models import User

# Create your models here.
class Source(models.Model):
    SOURCE_TYPES = (
        ('vk', 'ВКонтакте'),
        ('tg', 'Telegram'),
        ('other', 'Другое'),
    )
    title           = models.TextField(max_length=100, null=False)
    url             = models.URLField()
    type            = models.CharField(max_length=10, choices=SOURCE_TYPES)

    def __str__(self):
        return self.url

class SourceUsers(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    source          = models.ForeignKey(Source, on_delete=models.CASCADE)
    message_count   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} ({self.source.url})"
