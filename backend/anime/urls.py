from django.urls import path
from .views import browse_anime

urlpatterns = [
    path('browse/', browse_anime, name='browse_anime'),
]