from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("auctions.urls")),
    path('api/', include('auctions.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
