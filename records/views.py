from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ValorRecord

def index(request):
    return render(request, 'records/index.html')

class ValorRecordListView(generic.ListView):
    queryset = ValorRecord.objects.filter(status=2)
    template_name = 'records/index.html'
    context_object_name = 'valor_records'
    paginate_by = 6
