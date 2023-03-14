# Generated by Django 4.1 on 2022-10-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0048_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='closedAuction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closedAuction', to='auctions.auction'),
        ),
    ]
