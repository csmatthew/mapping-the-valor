from django.shortcuts import render
from django.http import JsonResponse
from valor_records.models import ValorRecord


def map_view(request):
    return render(request, 'mapper/map.html')


def valor_records_json(request):
    valor_records = ValorRecord.objects.all()
    data = [
        {
            'name': record.name,
            'record_type': record.record_type,
            'latitude': record.latitude,
            'longitude': record.longitude,
        }
        for record in valor_records
    ]
    return JsonResponse(data, safe=False)
