# Generated by Django 4.1 on 2022-09-16 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_auction_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='seller',
        ),
        migrations.AddField(
            model_name='auction',
            name='seller',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
