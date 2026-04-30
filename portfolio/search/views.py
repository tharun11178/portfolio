from django.shortcuts import render
from wagtail.models import Page


def search(request):
    search_query = request.GET.get('query', '')
    search_results = Page.objects.live().public().search(search_query) if search_query else Page.objects.none()

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })