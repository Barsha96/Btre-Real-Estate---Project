
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')), #anything that comes with listings/ will go to listings.urls
    path('admin/', admin.site.urls), #anything that comes with admin/ will go to admin.site.urls
]
