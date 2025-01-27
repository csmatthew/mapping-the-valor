from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, ApprovedPost
from django.core.serializers import serialize
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

# Visual
def monasteries_map(request):
    approved_posts = Post.objects.filter(status=2)
    monasteries_json = serialize('json', approved_posts, use_natural_foreign_keys=True)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

# Post editing capabilities


@login_required
def submit_for_approval(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.created_by:
        post.status = 1  # Set status to pending approval
        post.save()
    return redirect('post_detail', slug=post.slug)

@user_passes_test(lambda u: u.is_staff)
def approve_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 2  # Set status to published
    post.save()
    return redirect('post_detail', slug=post.slug)


# Public views
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

# Login/Logout
def account_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'You have signed out.', extra_tags='logout')
    return redirect('home')
