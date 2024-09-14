# Generated by Django 5.1 on 2024-09-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_makale_teslimalanpersonel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Resim Yükleme'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image1',
            field=models.ImageField(blank=True, default=False, null=True, upload_to='image'),
        ),
    ]