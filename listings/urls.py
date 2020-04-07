from django.urls import path
from . import views
#we are gonna tell te main url file that anything that has listings/ will look at this file
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]