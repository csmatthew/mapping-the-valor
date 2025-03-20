from django.shortcuts import render
from valor_records.models import ValorRecord


def index(request):
    return render(request, 'core/index.html')


def search_view(request):
    query = request.GET.get('search')
    results = []
    if query:
        results = ValorRecord.objects.filter(name__icontains=query)
    return render(
        request,
        'core/search_results.html',
        {'query': query, 'results': results}
    )
