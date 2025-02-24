from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import CreatePostForm, SearchForm
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish
from .models.valor_record import ValorRecord
from .models.monastery import Monastery
from .utils import get_previous_list_type


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
    query = request.GET.get('query', '')
    results = {
        'dioceses': [], 'archdeaconries': [], 'deaneries': [], 'parishes': [],
        'valor_records': [], 'monasteries': []
    }

    if query:
        results = {
            'dioceses': Diocese.objects.filter(name__icontains=query),
            'archdeaconries': Archdeaconry.objects.filter(
                name__icontains=query),
            'deaneries': Deanery.objects.filter(name__icontains=query),
            'parishes': Parish.objects.filter(name__icontains=query),
            'valor_records': ValorRecord.objects.filter(name__icontains=query),
            'monasteries': Monastery.objects.filter(
                monastery_name__icontains=query
            ),
        }

    return render(request, 'records/explore.html', {
        'query': query,
        'results': results
    })


def explore_provinces(request):
    query = request.GET.get('query', '')
    provinces = Province.objects.filter(name__icontains=query).order_by('name')
    previous_list_type = get_previous_list_type(request)
    return render(request, 'records/explore_list.html', {
        'title': 'Provinces',
        'items': provinces,
        'item_url_name': 'province_detail',
        'query': query,
        'previous_list_type': previous_list_type
    })


def explore_dioceses(request):
    query = request.GET.get('query', '')
    dioceses = Diocese.objects.filter(name__icontains=query).order_by('name')
    previous_list_type = get_previous_list_type(request)
    return render(request, 'records/explore_list.html', {
        'title': 'Dioceses',
        'items': dioceses,
        'item_url_name': 'diocese_detail',
        'query': query,
        'previous_list_type': previous_list_type
    })


def explore_archdeaconries(request):
    query = request.GET.get('query', '')
    archdeaconries = Archdeaconry.objects.filter(
        name__icontains=query).order_by('name')
    previous_list_type = get_previous_list_type(request)
    return render(request, 'records/explore_list.html', {
        'title': 'Archdeaconries',
        'items': archdeaconries,
        'item_url_name': 'archdeaconry_detail',
        'query': query,
        'previous_list_type': previous_list_type
    })


def explore_deaneries(request):
    query = request.GET.get('query', '')
    deaneries = Deanery.objects.filter(name__icontains=query).order_by('name')
    previous_list_type = get_previous_list_type(request)
    return render(request, 'records/explore_list.html', {
        'title': 'Deaneries',
        'items': deaneries,
        'item_url_name': 'deanery_detail',
        'query': query,
        'previous_list_type': previous_list_type
    })


def explore_parishes(request):
    query = request.GET.get('query', '')
    parishes = Parish.objects.filter(name__icontains=query).order_by('name')
    previous_list_type = get_previous_list_type(request)
    return render(request, 'records/explore_list.html', {
        'title': 'Parishes',
        'items': parishes,
        'item_url_name': 'parish_detail',
        'query': query,
        'previous_list_type': previous_list_type
    })


class HierarchyDetailView(DetailView):
    template_name = 'records/hierarchy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.object.__class__
        previous_list_type = get_previous_list_type(self.request)
        context['previous_list_type'] = previous_list_type
        if model == Province:
            context['children'] = Diocese.objects.filter(province=self.object)
            context['child_name'] = 'Dioceses'
            context['previous_list_type'] = previous_list_type
        elif model == Diocese:
            context['children'] = Archdeaconry.objects.filter(
                diocese=self.object
            )
            context['child_name'] = 'Archdeaconries'
            context['previous_list_type'] = previous_list_type
        elif model == Archdeaconry:
            context['children'] = Deanery.objects.filter(
                archdeaconry=self.object
            )
            context['child_name'] = 'Deaneries'
            context['previous_list_type'] = previous_list_type
        return context


class ValorRecordDetailView(DetailView):
    model = ValorRecord
    template_name = 'records/valorrecord_detail.html'


class MonasteryDetailView(DetailView):
    model = Monastery
    template_name = 'records/monastery_detail.html'
