# Generated by Django 4.1.1 on 2022-09-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_bidder_bidder_alter_bidder_listing_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidder',
            name='listing_bid',
        ),
        migrations.AddField(
            model_name='bidder',
            name='listing_bid',
            field=models.ManyToManyField(related_name='bid', to='auctions.listing'),
        ),
    ]
