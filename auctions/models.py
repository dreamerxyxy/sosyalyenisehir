from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta, datetime, timezone
from math import ceil

AUCTION_DURATION = 5

DEFAULT_STATUS = 'draft'
STATUS=[
    ('draft','Taslak'),
    ('published','Yayınlandı'),
    ('deleted','Silindi'),
]
DEFAULT_STATUS = 'Giriş'
STOK=[
    ('Çıkış','Çıkış'),
    ('Giriş','Giriş'),
]

DEFAULT_STATUS = 'Cenaze'
ETKINLIK=[
    ('Belediye', 'Belediye'),
    ('Cenaze','Cenaze'),
    ('Dernek', 'Dernek'),
    ('Etkinlik', 'Etkinlik'),
    ('Mevlüt','Mevlüt'),
    ('Muhtarlık', 'Muhtarlık'),
    ('Organizasyon','Organizasyon'),
    ('Yardımlaşma', 'Yardımlaşma'),

]

class Personel(models.Model):
    ad= models.CharField(null=False, blank=False, max_length=100,verbose_name='Lütfen Personelin Adınızı Giriniz')
    soyad = models.CharField(null=False, blank=False, max_length=100,verbose_name='Lütfen Personelin Soyadını Giriniz')
    telefon = models.CharField(max_length=20, blank=False, help_text='Telefon numarasını Giriniz',verbose_name='Telefon Numarası')

    def __str__(self):
        return f'{self.ad} {self.soyad}'

class Makale(models.Model):
    Etkinlikturu = models.CharField(default=DEFAULT_STATUS, choices=ETKINLIK, max_length=15, verbose_name='Etkinlik Türü')
    verilenmasa = models.PositiveIntegerField(null=True, blank=True, verbose_name='Verilen Masa')
    verilensandalye = models.PositiveIntegerField(null=True, blank=True, verbose_name='Sandalye')
    verilensemaver = models.PositiveIntegerField(null=True, blank=True, verbose_name='Semaver')
    verilencadir = models.PositiveIntegerField(null=True, blank=True, verbose_name='Çadır')
    verilensemsiye = models.PositiveIntegerField(null=True, blank=True, verbose_name='Şemsiye')
    verilensadirvan = models.PositiveIntegerField(null=True, blank=True, verbose_name='Şadırvan')
    verilencay = models.PositiveIntegerField(null=True, blank=True, verbose_name='Çay')
    verilenseker = models.PositiveIntegerField(null=True, blank=True, verbose_name='Şeker')
    verilensu = models.PositiveIntegerField(null=True, blank=True, verbose_name='Su')
    verilenbardak = models.PositiveIntegerField(null=True, blank=True, verbose_name='Bardak')
    verilenmasaortusu = models.PositiveIntegerField(null=True, blank=True, verbose_name=' Masa Örtüsü')
    verilenkaristirici = models.PositiveIntegerField(null=True, blank=True, verbose_name='Karıştırıcı')
    teslimtarihi = models.DateTimeField(null=True,blank=True,verbose_name='Malzeme Teslim Tarihi')
    teslimedenpersonel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name='teslimedenpersonel')
    guncellenmetarihi = models.DateTimeField(auto_now_add=True,verbose_name='Güncellenme Tarihi')
    teslimalanad = models.CharField(max_length=50, verbose_name='Teslim Alan Ad')
    teslimalansoyad = models.CharField(max_length=50, verbose_name='Soyad')
    teslimalantelefon = models.CharField(max_length=20, blank=False, help_text='Lütfen Numaranızı Giriniz', verbose_name='Telefon')
    teslimalanadres = models.CharField(max_length=250, verbose_name='Adres')
    image = models.ImageField(upload_to='image', null=True, blank=True, verbose_name='Resim Yükleme')
    alinanmasa = models.PositiveIntegerField(null=True, blank=True, verbose_name='Alınan  Masa')
    alinansandalye = models.PositiveIntegerField(null=True, blank=True, verbose_name='Sandalye')
    alinansemaver = models.PositiveIntegerField(null=True, blank=True, verbose_name='Semaver')
    alinancadir = models.PositiveIntegerField(null=True, blank=True, verbose_name='Çadır')
    alinansemsiye = models.PositiveIntegerField(null=True, blank=True, verbose_name='Şemsiye')
    alinansadirvan = models.PositiveIntegerField(null=True, blank=True, verbose_name='Şadırvan')
    teslimalmatarihi = models.DateTimeField(null=True,blank=True,verbose_name='Malzemenin Geri Alındığı Tarihi')
    teslimalanpersonel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name='teslimalanpersonel',null=True,blank=True)
    ekstranot = models.TextField(blank=True,null=True, verbose_name='Not Giriniz')
    aktif =models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = u"Sosyal Etkinlikler"
        verbose_name = u"Makale"

    def __str__(self):
        return f"{self.Etkinlikturu} Etkinliği  :{self.teslimalanad} : {self.teslimalansoyad} Telefon numarası: {self.teslimalantelefon} Adres:  {self.teslimalanadres} Verilen Tarih: {self.teslimtarihi} Teslim Eden {self.teslimedenpersonel}{self.aktif}"





class StokCategory(models.Model):
    group = models.CharField(max_length=50, blank=True, null=True,verbose_name=' Stok Kategori')

    class Meta:
        verbose_name_plural = u"Stok Kategorileri Giriş"
        verbose_name = u"Category"

    def __str__(self):
        return self.group

class Stock(models.Model):
    stokcategory = models.ForeignKey(StokCategory, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Stok Adı')
    quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Miktar')
    receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Başlangıç Giren Miktar')
    issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Başlangıç Çıkan Miktar')
    created_by =  models.ForeignKey(Personel, on_delete=models.CASCADE, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='son güncelleme tarihi')
    image = models.ImageField(upload_to='image', null=True, blank=True, verbose_name='Resim Yükleme')
    Not = models.TextField(blank=True,null=True,verbose_name='Açıklama')
    aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = u"Stok Kartları"
        verbose_name = u"Stock"


    def quantity(self):
        return self.receive_quantity - self.issue_quantity


    def __str__(self):
        return f"{self.stokcategory} {self.item_name}"

class Stocktype(models.Model):
    item_name= models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True)
    stok = models.CharField(default=DEFAULT_STATUS, choices=STOK, max_length=7, verbose_name='Fiş Türü')
    receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name=' Giren Miktar')
    issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Çıkan Miktar')
    created_by = models.ForeignKey(Personel, on_delete=models.CASCADE, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='son güncelleme tarihi')
    Not = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = u"Stok Giriş Çıkış Fişi"
        verbose_name = u"Stocktype"


    def __str__(self):
        return f"{self.item_name}{self.stok}"



class User(AbstractUser):
    phone = models.CharField(max_length=20,blank=False, help_text='Contact phone number')
    adres= models.TextField(null=True,blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    is_verified=models.BooleanField(default=False)
    code=models.CharField(max_length=8,blank=True,null=True)
    watchlist = models.ManyToManyField(
        'AuctionListing', blank=True, related_name="userWatchlist")

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} : {self.name}"


class AuctionListing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    ended=models.DateTimeField()
    startBid = models.DecimalField(default=1.1,decimal_places=2, max_digits=7)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.SET("(deleted)"),
                               blank=True,
                               null=True,
                               related_name="auction_winner",
                               related_query_name="auction_winner")
    final_value = models.IntegerField(blank=True, null=True)
    image1 = models.ImageField(
        upload_to='image',
        null=True,
        blank=True,
        default=False,
    )
    image2 = models.ImageField(
        upload_to='image',
        null=True,
        blank=True,
        default=False,
    )
    image3 = models.ImageField(
        upload_to='image',
        null=True,
        blank=True,
        default=False,
    )
    image4 = models.ImageField(
        upload_to='image',
        null=True,
        blank=True,
        default=False,
    )
    active = models.BooleanField()

    def resolve(self):
        if self.active:
            # If expired
            if self.has_expired():
                # Define winner
                highest_bid = Bid.objects.filter(auctionListing=self).order_by('-bidValue').order_by('date').first()
                if highest_bid:
                    self.winner = highest_bid.user
                    self.final_value = highest_bid.bidValue
                self.active = False
                self.save()

    # Helper function that determines if the auction has expired
    def has_expired(self):
        now = datetime.now(timezone.utc)
        expiration = self.ended + timedelta(minutes=AUCTION_DURATION)
        if now > expiration:
            return True
        else:
            return False

    # Returns the ceiling of remaining_time in minutes
    @property
    def remaining_minutes(self):
        if self.active:
            now = datetime.now(timezone.utc)
            expiration = self.ended + timedelta(minutes=AUCTION_DURATION)
            minutes_remaining = ceil((expiration - now).total_seconds() / 60)
            return (minutes_remaining)
        else:
            return (0)


    def __str__(self):
        return f"{self.id} : {self.name} in {self.category.name}\nPosted at : {self.date}\nValue : {self.startBid}\nDescription : {self.description}\nPosted By : {self.user.username} Active Status: {self.active}"


class Bid(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bidValue = models.DecimalField(decimal_places=2, max_digits=7)
    auctionListing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : {self.user.username} bid {self.bidValue} on {self.auctionListing.name} at {self.date}"


class Comment(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionListing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE)
    commentValue = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id} : {self.user.username} commented on {self.auctionListing.name} posted by {self.auctionListing.user.username} at {self.date} : {self.commentValue}"

class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title