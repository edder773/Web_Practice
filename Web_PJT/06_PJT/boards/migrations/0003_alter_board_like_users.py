# Generated by Django 3.2.13 on 2023-04-14 03:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_board_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(related_name='like_board', to=settings.AUTH_USER_MODEL),
        ),
    ]