# Generated by Django 3.2 on 2022-03-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_bid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
