from django.shortcuts import render, redirect
from .models import Content
from .utils import fetch_anime, fetch_manga, fetch_manhwa


# ANIME
def anime_page(request):
    query = request.GET.get('q')
    page = int(request.GET.get('page', 1))

    results = fetch_anime(query, page)

    if request.method == "POST":

        # ➕ ADD
        if "title" in request.POST:
            Content.objects.create(
                title=request.POST.get("title"),
                image=request.POST.get("image"),
                content_type="anime"
            )
            return redirect(request.path)

        # 🔁 TOGGLE
        if "toggle_id" in request.POST:
            obj = Content.objects.get(id=request.POST.get("toggle_id"))
            obj.is_done = not obj.is_done
            obj.save()
            return redirect(request.path)

    watched = Content.objects.filter(content_type="anime", is_done=True)
    not_watched = Content.objects.filter(content_type="anime", is_done=False)

    return render(request, "tracking/anime.html", {
        "results": results,
        "watched": watched,
        "not_watched": not_watched,
        "query": query,
        "page": page,
        "type": "ANIME"
    })


# 📚 MANGA
def manga_page(request):
    query = request.GET.get('q')
    page = int(request.GET.get('page', 1))

    results = fetch_manga(query, page)

    if request.method == "POST":

        if "title" in request.POST:
            Content.objects.create(
                title=request.POST.get("title"),
                image=request.POST.get("image"),
                content_type="manga"
            )
            return redirect(request.path)

        if "toggle_id" in request.POST:
            obj = Content.objects.get(id=request.POST.get("toggle_id"))
            obj.is_done = not obj.is_done
            obj.save()
            return redirect(request.path)

    watched = Content.objects.filter(content_type="manga", is_done=True)
    not_watched = Content.objects.filter(content_type="manga", is_done=False)

    return render(request, "tracking/anime.html", {
        "results": results,
        "watched": watched,
        "not_watched": not_watched,
        "query": query,
        "page": page,
        "type": "MANGA"
    })


# 🇰🇷 MANHWA
def manhwa_page(request):
    query = request.GET.get('q')
    page = int(request.GET.get('page', 1))

    results = fetch_manhwa(query, page)   # 🔥 already filtered

    if request.method == "POST":

        if "title" in request.POST:
            Content.objects.create(
                title=request.POST.get("title"),
                image=request.POST.get("image"),
                content_type="manhwa"
            )
            return redirect(request.path)

        if "toggle_id" in request.POST:
            obj = Content.objects.get(id=request.POST.get("toggle_id"))
            obj.is_done = not obj.is_done
            obj.save()
            return redirect(request.path)

    watched = Content.objects.filter(content_type="manhwa", is_done=True)
    not_watched = Content.objects.filter(content_type="manhwa", is_done=False)

    return render(request, "anime.html", {
        "results": results,
        "watched": watched,
        "not_watched": not_watched,
        "query": query,
        "page": page,
        "type": "MANHWA"
    })