from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, ApprovedPost, FinancialDetail
from django.core.serializers import serialize
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .utils import fetch_wikipedia_image
from .forms import FinancialDetailForm

# Visual
def monasteries_map(request):
    approved_posts = Post.objects.filter(status=2)
    monasteries_json = serialize('json', approved_posts, use_natural_foreign_keys=True)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

# Public views
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not post.image_url:
        post.image_url = fetch_wikipedia_image(post.name, post.house_type.name)
        post.save()
    if request.method == 'POST':
        form = FinancialDetailForm(request.POST)
        if form.is_valid():
            financial_detail = form.save(commit=False)
            financial_detail.post = post
            financial_detail.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = FinancialDetailForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

# Login/Logout
def account_logout(request):
    logout(request)
    return redirect('home')

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

