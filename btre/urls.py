
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')), #anything that comes with listings/ will go to listings.urls
    path('accounts/', include('accounts.urls')), #anything that comes with accounts/ will go to listings.urls
    path('admin/', admin.site.urls), #anything that comes with admin/ will go to admin.site.urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
