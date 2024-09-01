# Generated by Django 5.1 on 2024-08-31 15:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayınlandı'), ('deleted', 'Silindi')], default='Cenaze', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, verbose_name='Lütfen Personelin Adınızı Giriniz')),
                ('soyad', models.CharField(max_length=100, verbose_name='Lütfen Personelin Soyadını Giriniz')),
                ('telefon', models.CharField(help_text='Telefon numarasını Giriniz', max_length=20, verbose_name='Telefon Numarası')),
            ],
        ),
        migrations.CreateModel(
            name='StokCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=50, null=True, verbose_name=' Stok Kategori')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Stok Kategorileri Giriş',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(help_text='Contact phone number', max_length=20)),
                ('adres', models.TextField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('ended', models.DateTimeField()),
                ('startBid', models.DecimalField(decimal_places=2, default=1.1, max_digits=7)),
                ('description', models.CharField(max_length=250)),
                ('final_value', models.IntegerField(blank=True, null=True)),
                ('image1', models.FileField(blank=True, default=False, null=True, upload_to='image')),
                ('image2', models.ImageField(blank=True, default=False, null=True, upload_to='image')),
                ('image3', models.ImageField(blank=True, default=False, null=True, upload_to='image')),
                ('image4', models.ImageField(blank=True, default=False, null=True, upload_to='image')),
                ('active', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=models.SET('(deleted)'), related_name='auction_winner', related_query_name='auction_winner', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.category')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='userWatchlist', to='auctions.auctionlisting'),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('bidValue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('auctionListing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('commentValue', models.CharField(max_length=250)),
                ('auctionListing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etkinlikturu', models.CharField(choices=[('Cenaze', 'Cenaze'), ('Mevlüt', 'Mevlüt'), ('Organizasyon', 'Organizasyon'), ('Dernek', 'Dernek'), ('Muhtarlık', 'Muhtarlık'), ('Belediye', 'Belediye'), ('Yardımlaşma', 'Yardımlaşma')], default='Cenaze', max_length=15, verbose_name='Etkinlik Türü')),
                ('verilenmasa', models.PositiveIntegerField(blank=True, null=True, verbose_name='Verilen Masa')),
                ('verilensandalye', models.PositiveIntegerField(blank=True, null=True, verbose_name='Sandalye')),
                ('verilensemaver', models.PositiveIntegerField(blank=True, null=True, verbose_name='Semaver')),
                ('verilencadir', models.PositiveIntegerField(blank=True, null=True, verbose_name='Çadır')),
                ('verilensemsiye', models.PositiveIntegerField(blank=True, null=True, verbose_name='Şemsiye')),
                ('verilensadirvan', models.PositiveIntegerField(blank=True, null=True, verbose_name='Şadırvan')),
                ('verilencay', models.PositiveIntegerField(blank=True, null=True, verbose_name='Çay')),
                ('verilenseker', models.PositiveIntegerField(blank=True, null=True, verbose_name='Şeker')),
                ('verilensu', models.PositiveIntegerField(blank=True, null=True, verbose_name='Su')),
                ('verilenbardak', models.PositiveIntegerField(blank=True, null=True, verbose_name='Bardak')),
                ('verilenmasaortusu', models.PositiveIntegerField(blank=True, null=True, verbose_name=' Masa Örtüsü')),
                ('verilenkaristirici', models.PositiveIntegerField(blank=True, null=True, verbose_name='Karıştırıcı')),
                ('teslimtarihi', models.DateTimeField(auto_now_add=True, verbose_name='Malzeme Teslim Tarihi')),
                ('guncellenmetarihi', models.DateTimeField(auto_now_add=True, verbose_name='Güncellenme Tarihi')),
                ('teslimalanad', models.CharField(max_length=50, verbose_name='Teslim Alan Ad')),
                ('teslimalansoyad', models.CharField(max_length=50, verbose_name='Soyad')),
                ('teslimalantelefon', models.CharField(help_text='Lütfen Numaranızı Giriniz', max_length=20, verbose_name='Telefon')),
                ('teslimalanadres', models.CharField(max_length=250, verbose_name='Adres')),
                ('alinanmasa', models.PositiveIntegerField(blank=True, null=True, verbose_name='Alınan  Masa')),
                ('alinansandalye', models.PositiveIntegerField(blank=True, null=True, verbose_name='Sandalye')),
                ('alinansemaver', models.PositiveIntegerField(blank=True, null=True, verbose_name='Semaver')),
                ('alinancadir', models.PositiveIntegerField(blank=True, null=True, verbose_name='Çadır')),
                ('alinansemsiye', models.PositiveIntegerField(blank=True, null=True, verbose_name='Şemsiye')),
                ('alinansadirvan', models.PositiveIntegerField(blank=True, null=True, verbose_name='Şadırvan')),
                ('teslimalmatarihi', models.DateTimeField(auto_now_add=True, verbose_name='Malzemenin Geri Alındığı Tarihi')),
                ('ekstranot', models.TextField(blank=True, null=True, verbose_name='Not Giriniz')),
                ('aktif', models.BooleanField(default=True)),
                ('teslimalanpersonel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teslimalanpersonel', to='auctions.personel')),
                ('teslimedenpersonel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teslimedenpersonel', to='auctions.personel')),
            ],
            options={
                'verbose_name': 'Makale',
                'verbose_name_plural': 'Sosyal Etkinlikler',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Stok Adı')),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Başlangıç Giren Miktar')),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Başlangıç Çıkan Miktar')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='son güncelleme tarihi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Resim Yükleme')),
                ('Not', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('aktif', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.personel')),
                ('stokcategory', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.stokcategory')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stok Kartları',
            },
        ),
        migrations.CreateModel(
            name='Stocktype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stok', models.CharField(choices=[('Çıkış', 'Çıkış'), ('Giriş', 'Giriş')], default='Cenaze', max_length=7, verbose_name='Fiş Türü')),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name=' Giren Miktar')),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Çıkan Miktar')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='son güncelleme tarihi')),
                ('Not', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('aktif', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.personel')),
                ('item_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.stock')),
            ],
            options={
                'verbose_name': 'Stocktype',
                'verbose_name_plural': 'Stok Giriş Çıkış Fişi',
            },
        ),
    ]