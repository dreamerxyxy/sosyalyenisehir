# Generated by Django 5.1 on 2024-08-31 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_makale_teslimtarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='teslimalanpersonel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teslimalanpersonel', to='auctions.personel'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='teslimalmatarihi',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Malzemenin Geri Alındığı Tarihi'),
        ),
    ]