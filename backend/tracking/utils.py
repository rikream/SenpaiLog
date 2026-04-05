#this is for tracking for api calls
import requests

URL = "https://graphql.anilist.co"
def fetch_anime(query=None, page=1):
    graphql_query = {
        "query": """
        query ($search: String, $page: Int) {
          Page(page: $page, perPage: 12) {
            media(search: $search, type: ANIME) {
              title { romaji }
              coverImage { large }
            }
          }
        }
        """,
        "variables": {
            "search": query,
            "page": page
        }
    }

    response = requests.post(URL, json=graphql_query)
    data = response.json()

    return [
        {
            "title": item["title"]["romaji"],
            "image": item["coverImage"]["large"]
        }
        for item in data["data"]["Page"]["media"]
    ]

def fetch_manga(query=None, page=1):
    graphql_query = {
        "query": """
        query ($search: String, $page: Int) {
          Page(page: $page, perPage: 12) {
            media(search: $search, type: MANGA) {
              title { romaji }
              coverImage { large }
              countryOfOrigin
            }
          }
        }
        """,
        "variables": {
            "search": query,
            "page": page
        }
    }

    response = requests.post(URL, json=graphql_query)
    data = response.json()

    return [
        {
            "title": item["title"]["romaji"],
            "image": item["coverImage"]["large"]
        }
        for item in data["data"]["Page"]["media"]
        if item["countryOfOrigin"] != "KR"   # exclude manhwa
    ]

def fetch_manhwa(query=None, page=1):
    graphql_query = {
        "query": """
        query ($search: String, $page: Int) {
          Page(page: $page, perPage: 12) {
            media(search: $search, type: MANGA) {
              title { romaji }
              coverImage { large }
              countryOfOrigin
            }
          }
        }
        """,
        "variables": {
            "search": query,
            "page": page
        }
    }

    response = requests.post(URL, json=graphql_query)
    data = response.json()

    return [
        {
            "title": item["title"]["romaji"],
            "image": item["coverImage"]["large"]
        }
        for item in data["data"]["Page"]["media"]
        if item["countryOfOrigin"] == "KR"   # only manhwa
    ]