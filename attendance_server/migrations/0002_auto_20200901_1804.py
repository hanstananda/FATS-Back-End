# Generated by Django 3.1 on 2020-09-01 10:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance_server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseschedule',
            old_name='course',
            new_name='name',
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
