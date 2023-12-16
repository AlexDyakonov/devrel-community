# Generated by Django 5.0 on 2023-12-16 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_data', to='api.event')),
            ],
        ),
    ]
