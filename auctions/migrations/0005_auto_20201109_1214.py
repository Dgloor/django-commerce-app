# Generated by Django 3.1.3 on 2020-11-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201108_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('BOOKS', 'Books'), ('MUSIC', 'Music'), ('GAMES', 'Games'), ('ELECTRONICS', 'Electronics'), ('HOME', 'Home'), ('TOYS', 'Toys'), ('SPORTS', 'Sports'), ('FASHION', 'Fashion')], max_length=200, null=True, verbose_name='Category'),
        ),
    ]
