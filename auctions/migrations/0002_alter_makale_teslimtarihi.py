# Generated by Django 5.1 on 2024-08-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='teslimtarihi',
            field=models.DateTimeField(verbose_name='Malzeme Teslim Tarihi'),
        ),
    ]
