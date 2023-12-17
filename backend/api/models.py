from django.db import models
from users.models import User
from django.core.validators import FileExtensionValidator
from users.models import User
import json


def event_banner_directory_path(instance, filename):
    return 'event_banners/{0}/{1}'.format(instance.id, filename)

# Create your models here.
class Event(models.Model):
    EVENT_TYPES = (
        ('conference', 'Конференция'),
        ('hackathon', 'Хакатон'),
        ('webinar', 'Вебинар'),
        ('meetup', 'Митап'),
        ('lecture', 'Лекция'),
        ('exhibition', 'Выставка'),
        ('training', 'Тренинг'),
        ('discussion', 'Дискуссия'),
        ('forum', 'Форум'),
        ('job_opening', 'Вакансия'),
        ('certification', 'Сертификация'),
        ('testing', 'Тестирование'),
        ('internship', 'Стажировки'),
    )

    title               = models.CharField(max_length=255, null=False, blank=False)
    speakers            = models.CharField(max_length=255, null=False, blank=False)
    banner              = models.ImageField(
        upload_to=event_banner_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'tiff', 'svg'])]
    )
    description         = models.TextField(max_length=2000, null=False, blank=False)
    event_type          = models.CharField(max_length=20, choices=EVENT_TYPES)
    location            = models.CharField(max_length=255, null=True, blank=True)
    start_time          = models.DateTimeField(null=False, blank=False)
    end_time            = models.DateTimeField(null=False, blank=False)
    participants        = models.ManyToManyField(User, related_name='events_participated', blank=True)
    social_media_link   = models.URLField(blank=True)


    def get_banner_url(self):
        if self.banner:
            return self.banner.url
        return ''

    def __str__(self):
        return self.title

class FormFields(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_data')
    data = models.JSONField()

    def set_data(self, data_dict):
        self.data = json.dumps(data_dict)

    def get_data(self):
        return json.loads(self.data)

    def __str__(self):
        return f"Fields for Event: {self.event.title}"