from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, SearchForm
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish
from .models.valor_record import ValorRecord
from .models.monastery import Monastery


def index(request):
    return render(request, 'records/map.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the map view
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})


# For search.html
def search(request):
    form = SearchForm()
    results = {
        'dioceses': [], 'archdeaconries': [], 'deaneries': [], 'parishes': [],
        'valor_records': [], 'monasteries': []
    }

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = {
                'dioceses': Diocese.objects.filter(
                    name__icontains=query
                ),
                'archdeaconries': Archdeaconry.objects.filter(
                    name__icontains=query
                ),
                'deaneries': Deanery.objects.filter(
                    name__icontains=query
                ),
                'parishes': Parish.objects.filter(
                    name__icontains=query
                ),
                'valor_records': ValorRecord.objects.filter(
                    name__icontains=query
                ),
                'monasteries': Monastery.objects.filter(
                    monastery_name__icontains=query),
            }

    return render(
        request, 'records/search.html', {'form': form, 'results': results}
    )


# For explore.html
def explore(request):
    provinces = Province.objects.all()
    return render(request, 'records/explore.html', {'provinces': provinces})


def province_detail(request, pk):
    province = get_object_or_404(Province, pk=pk)
    dioceses = Diocese.objects.filter(province=province)
    return render(request, 'records/detail/province_detail.html', {
        'province': province,
        'dioceses': dioceses
    })


def archdeaconry_detail(request, pk):
    archdeaconry = get_object_or_404(Archdeaconry, pk=pk)
    deaneries = Deanery.objects.filter(archdeaconry=archdeaconry)
    return render(request, 'records/detail/archdeaconry_detail.html', {
        'archdeaconry': archdeaconry,
        'deaneries': deaneries
    })
