# Generated by Django 4.1 on 2022-09-20 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_remove_auction_categories_auction_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='is_active',
        ),
    ]
