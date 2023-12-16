# Generated by Django 5.0 on 2023-12-16 19:58

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReffLink',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=5, max_length=11, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]
