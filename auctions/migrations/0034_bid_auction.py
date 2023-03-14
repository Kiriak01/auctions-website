# Generated by Django 4.1 on 2022-09-21 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_remove_bid_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='auctions.auction'),
        ),
    ]
