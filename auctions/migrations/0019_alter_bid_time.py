# Generated by Django 4.1 on 2022-09-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_rename_userid_bid_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
