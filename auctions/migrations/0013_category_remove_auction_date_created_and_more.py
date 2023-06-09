# Generated by Django 4.1 on 2022-09-08 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_user_is_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='auction',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='title',
        ),
        migrations.AddField(
            model_name='auction',
            name='bidders',
            field=models.ManyToManyField(related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auction',
            name='buy_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='currently',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='ends',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='first_bid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='itemId',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='number_of_bids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auction',
            name='started',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bidder_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='seller_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='scn',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='bids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
        migrations.AddField(
            model_name='auction',
            name='categories',
            field=models.ManyToManyField(to='auctions.category'),
        ),
    ]
