from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.serializers import serialize

def monasteries_map(request):
    monasteries = Post.objects.filter(status=2)  # Only include published posts
    monasteries_json = serialize('json', monasteries)
    return render(request, 'blog/home.html', {'monasteries': monasteries_json})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.status = 0  # Set status to Draft
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})