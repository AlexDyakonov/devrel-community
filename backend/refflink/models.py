import json
import uuid
from django.db import models
from shortuuid.django_fields import ShortUUIDField


class ReffLink(models.Model):
    id = ShortUUIDField(primary_key=True, length=5, max_length=11)
    name = models.CharField(max_length=255, null=False, blank=False)
    count = models.IntegerField(default=0)
    link = models.CharField(max_length=255, null=False)

    def set_data(self, data_dict):
        self.data = json.dumps(data_dict)

    def get_data(self):
        return json.loads(self.data)

    def __str__(self):
        return f"ReffLink: {self.name} -> {self.link}"
