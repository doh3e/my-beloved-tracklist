from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-music', views.addmusic),
    path('my-playlist', views.myplaylist),
    path('music-calendar',views.musiccalendar),
]
