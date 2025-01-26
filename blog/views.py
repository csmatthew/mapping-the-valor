from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, ApprovedPost, Holding
from django.core.serializers import serialize
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from .forms import PostForm, HoldingForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

# Visual
def monasteries_map(request):
    approved_posts = Post.objects.filter(status=2)
    monasteries_json = serialize('json', approved_posts, use_natural_foreign_keys=True)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(status=2)  

    if query:
        posts = posts.filter(
            Q(name__icontains=query) |
            Q(religious_order__name__icontains=query) |
            Q(house_type__name__icontains=query) |
            Q(nearest_town__icontains=query) |
            Q(county__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'query': query})

# Post editing capabilities
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


# login views
@login_required
def view_drafts(request):
    drafts = Post.objects.filter(created_by=request.user, status=0)  # Filter drafts by the logged-in user
    return render(request, 'blog/view_drafts.html', {'drafts': drafts})

@login_required
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        holding_form = HoldingForm(request.POST)
        if 'save_draft' in request.POST and post_form.is_valid():
            post = post_form.save(commit=False)
            post.last_updated_by = request.user
            if not request.user.is_staff:
                post.status = 0  # Save as draft for non-admin users
            post.save()
            return redirect('post_detail', slug=post.slug)
        elif 'submit_approval' in request.POST and post_form.is_valid():
            post = post_form.save(commit=False)
            post.last_updated_by = request.user
            post.status = 1  # Set status to pending approval
            post.save()
            return redirect('post_detail', slug=post.slug)
        elif 'add_holding' in request.POST and holding_form.is_valid():
            holding = holding_form.save(commit=False)
            holding.monastery = post
            holding.save()
            return redirect('post_detail', slug=post.slug)
    else:
        post_form = PostForm(instance=post)
        holding_form = HoldingForm()
    return render(request, 'blog/update_post.html', {'post_form': post_form, 'holding_form': holding_form, 'post': post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.status != 2:  # If the post is not approved
        post = post.approved_version
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_holding(request, monastery_id):
    monastery = get_object_or_404(Post, pk=monastery_id)
    if request.method == 'POST':
        form = HoldingForm(request.POST)
        if form.is_valid():
            holding = form.save(commit=False)
            holding.monastery = monastery
            holding.save()
            return redirect('post_detail', slug=monastery.slug)
    else:
        form = HoldingForm()
    return render(request, 'blog/add_holding.html', {'form': form, 'monastery': monastery})

# Login/Logout
def account_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'You have signed out.', extra_tags='logout')
    return redirect('home')



