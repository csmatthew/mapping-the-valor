from django.shortcuts import render, redirect
from .forms import CreatePostForm


def index(request):
    return render(request, 'records/map.html')


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the map view
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})
