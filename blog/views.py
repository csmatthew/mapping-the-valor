from django.shortcuts import render, redirect
from .models import Post
from django.core.serializers import serialize
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json

def monasteries_map(request):
    monasteries = Post.objects.filter(status=2)  # Filter for published posts
    monasteries_json = serialize('json', monasteries)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.last_updated_by = request.user  # Set last_updated_by
            post.status = 0  # Set status to Draft
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def view_drafts(request):
    drafts = Post.objects.filter(created_by=request.user, status=0)  # Filter drafts by the logged-in user
    return render(request, 'blog/view_drafts.html', {'drafts': drafts})
