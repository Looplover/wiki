# Generated by Django 4.1.1 on 2022-09-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_remove_bidder_listing_bid_bidder_listing_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(related_name='watchuser', to='auctions.listing'),
        ),
    ]
