from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm


def index(request):
    return render(request, 'records/map.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the map view
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})
