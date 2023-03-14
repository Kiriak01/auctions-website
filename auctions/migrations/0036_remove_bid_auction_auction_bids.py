# Generated by Django 4.1 on 2022-09-21 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_remove_auction_bidders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]