# Generated by Django 5.0 on 2023-12-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Id тг'),
        ),
    ]