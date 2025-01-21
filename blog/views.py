from django.shortcuts import render
from .models import Post
from django.core.serializers import serialize

def monasteries_map(request):
    monasteries = Post.objects.all()
    monasteries_json = serialize('json', monasteries)
    return render(request, 'blog/map.html', {'monasteries': monasteries_json})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})