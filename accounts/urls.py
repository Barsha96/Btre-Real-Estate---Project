#note- an app doesnt come with urls.py so we had to create one. which was also done in all other apps except btre which is our project
from django.urls import path
from . import views
#we are gonna tell te main url file that anything that has listings/ will look at this file
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]