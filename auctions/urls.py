from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('verify_code/', views.verify_code,name="verify_code"),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('password_reset/',views.password_reset_request,name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auctions/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auctions/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auctions/password_reset_complete.html'), name='password_reset_complete'),
    path("createListing", views.createListing, name="createListing"),
    path("details/<int:id>", views.details, name="details"),
    path("categories", views.categories, name="categories"),
    path("filter/<str:name>", views.filter, name="filter"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("end/<int:itemId>", views.end, name="end"),
    path("all", views.all, name="all"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watch", views.watch, name="watch"),
    path("my_auctions/", views.my_auctions, name='my_auctions'),
    path("my_bids/", views.my_bids, name='my_bids'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

