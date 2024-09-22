# Generated by Django 5.1 on 2024-09-22 19:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="followers",
            field=models.ManyToManyField(
                related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
