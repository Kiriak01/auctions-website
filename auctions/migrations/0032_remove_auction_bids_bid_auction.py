# Generated by Django 4.1 on 2022-09-20 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_remove_bid_amount_remove_bid_time_remove_bid_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bids',
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='auctions.auction'),
        ),
    ]
