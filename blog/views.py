from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.serializers import serialize
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json
from .forms import PostForm

def monasteries_map(request):
    monasteries = Post.objects.filter(status=2)  # Filter for published posts
    monasteries_json = serialize('json', monasteries, use_natural_foreign_keys=True)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

def post_list(request):
    posts = Post.objects.filter(status=2)  # Filter for published posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.last_updated_by = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def view_drafts(request):
    drafts = Post.objects.filter(created_by=request.user, status=0)  # Filter drafts by the logged-in user
    return render(request, 'blog/view_drafts.html', {'drafts': drafts})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_updated_by = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})