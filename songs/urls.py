from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:song_id>/', views.song_detail, name='song_detail'),
    path('<int:song_id>/download/', views.song_download, name='song_download'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
     path('<int:song_id>/assign/', views.assign_song_to_album, name='assign_song_to_album'),
]
