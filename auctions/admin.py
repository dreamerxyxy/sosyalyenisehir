from django.contrib import admin
from .models import Category, AuctionListing, User, Comment, Bid,Carousel,Makale,StokCategory,Stock,Stocktype,Personel
from import_export.admin import ImportExportModelAdmin

class MakaleAdmin(ImportExportModelAdmin):
    list_display = ('Etkinlikturu', 'teslimtarihi', 'teslimedenpersonel', 'teslimalanad', 'teslimalansoyad', 'teslimalantelefon','aktif','teslimalanpersonel','teslimalmatarihi')
    list_per_page = 50
    list_filter = ['Etkinlikturu', 'teslimtarihi','aktif']
    date_hierarchy = 'teslimtarihi'
    search_fields = ('teslimedenpersonel', 'teslimalanad', 'teslimalansoyad')
    list_display_links = ('Etkinlikturu', 'teslimedenpersonel', 'teslimalanad', 'teslimalansoyad', 'teslimalantelefon','aktif','teslimalanpersonel','teslimalmatarihi')
    actions_on_bottom = True
    actions_on_top = True




class StockAdmin(ImportExportModelAdmin):
    list_display = ('stokcategory', 'item_name', 'quantity', 'receive_quantity', 'issue_quantity','created_by','last_updated')
    list_per_page = 50
    list_filter = ['stokcategory','item_name']
    date_hierarchy = 'last_updated'
    exclude = ('last_updated',)
    search_fields = ['item_name',]
    list_display_links = ('item_name', 'stokcategory')
    actions_on_bottom = True
    actions_on_top = True



class StockTypeAdmin(ImportExportModelAdmin):
    list_display = ('item_name', 'stok', 'receive_quantity', 'issue_quantity','created_by','last_updated')
    list_per_page = 50
    list_filter = ['stok','item_name']
    date_hierarchy = 'last_updated'
    exclude = ('last_updated',)
    search_fields = ['item_name']
    list_display_links = ('item_name', 'stok','receive_quantity','issue_quantity','created_by')
    actions_on_bottom = True
    actions_on_top = True



admin.site.register(Personel)
admin.site.register(Makale,MakaleAdmin)
admin.site.register(StokCategory)
admin.site.register(Stock,StockAdmin)
admin.site.register(Stocktype,StockTypeAdmin)

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'username', 'age', 'is_staff','is_verified','adres','phone']

class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'cover_image',
        'status',
    ]
    list_filter = ['status', ]
    list_editable = list_filter

admin.site.register(User,UserAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)