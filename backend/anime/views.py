from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

def browse_anime(request):
    return render(request, "anime/browse_anime.html")