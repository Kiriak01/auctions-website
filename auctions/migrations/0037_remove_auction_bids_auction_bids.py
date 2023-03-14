# Generated by Django 4.1 on 2022-09-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0036_remove_bid_auction_auction_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bids',
        ),
        migrations.AddField(
            model_name='auction',
            name='bids',
            field=models.ManyToManyField(to='auctions.bid'),
        ),
    ]
