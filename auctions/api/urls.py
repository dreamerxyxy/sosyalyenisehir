from django.urls import path
from auctions.api import views as api_views

urlpatterns = [
    path('personel/<int:pk>',api_views.PersonelDetailAPIView.as_view(), name='personel-detay'),
    path('personel/', api_views.PersonelListCreateAPIView.as_view(), name='personel-listesi'),
    path('makaleler/',api_views.MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('makaleler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name='makale-detay'),
]