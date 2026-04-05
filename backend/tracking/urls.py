from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.anime_page, name='anime_track'),
    path('manga/', views.manga_page, name='manga_track'),
    path('manhwa/', views.manhwa_page, name='manhwa_track'),
]