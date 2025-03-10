from django.shortcuts import render, get_object_or_404
from .models import ValorRecord


def valor_record_detail(request, slug):
    valor_record = get_object_or_404(ValorRecord, slug=slug)
    return render(request, 'valor_records/valor_record_detail.html', {'valor_record': valor_record})
