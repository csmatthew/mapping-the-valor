from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

def monasteries_map(request):
    return render(request, 'records/monasteries_map.html')
