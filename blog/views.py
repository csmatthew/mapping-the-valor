from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status=1)  # Only show published posts
    return render(request, 'blog/post_list.html', {'posts': posts})