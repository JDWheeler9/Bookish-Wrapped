from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the search index.")

# Example of a working GET call
def titleSearch(request, title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)