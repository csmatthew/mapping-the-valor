from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, FinancialDetail
from django.core.serializers import serialize
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .utils import fetch_wikipedia_image
from .forms import FinancialDetailForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

# Visual
def monasteries_map(request):
    approved_posts = Post.objects.filter(status=2)
    monasteries_json = serialize('json', approved_posts, use_natural_foreign_keys=True)
    return render(request, 'blog/index.html', {'monasteries': monasteries_json})

# post_detail
@csrf_exempt  # Exempt CSRF for simplicity, though you should secure this in production
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Fetching image if missing (your existing code)
    if not post.image_url:
        post.image_url = fetch_wikipedia_image(post.name, post.house_type.name)
        post.save()

    if request.method == 'POST':
        # Log the incoming POST data
        logger.debug(f"POST data: {request.POST}")

        # Handling update
        if 'update_detail' in request.POST:
            detail_id = request.POST.get('detail_id')
            logger.debug(f"Detail ID for update: {detail_id}")
            
            # Check if the detail ID exists and is valid
            if not detail_id:
                return JsonResponse({'success': False, 'message': 'Detail ID is missing'})

            try:
                detail = get_object_or_404(FinancialDetail, id=detail_id)
            except FinancialDetail.DoesNotExist:
                logger.error(f"FinancialDetail with ID {detail_id} not found.")
                return JsonResponse({'success': False, 'message': 'Detail not found'})

            form = FinancialDetailForm(request.POST, instance=detail)
            if form.is_valid():
                form.save()
                # Returning updated detail as JSON response for DOM update
                return JsonResponse({
                    'success': True,
                    'id': detail.id,
                    'holding_title': detail.holding_title,
                    'holding_pounds': detail.holding_pounds,
                    'holding_shillings': detail.holding_shillings,
                    'holding_pence': detail.holding_pence,
                    'total_lsd': detail.total_lsd,
                    'message': 'Detail updated successfully'
                })
            else:
                logger.error(f"Invalid form for update: {form.errors}")
                return JsonResponse({'success': False, 'message': 'Form is invalid'})

        # Handling delete
        elif 'delete_detail' in request.POST:
            detail_id = request.POST.get('detail_id')
            logger.debug(f"Detail ID for delete: {detail_id}")
            
            # Check if the detail ID exists and is valid
            if not detail_id:
                return JsonResponse({'success': False, 'message': 'Detail ID is missing'})

            try:
                detail = get_object_or_404(FinancialDetail, id=detail_id)
            except FinancialDetail.DoesNotExist:
                logger.error(f"FinancialDetail with ID {detail_id} not found.")
                return JsonResponse({'success': False, 'message': 'Detail not found'})

            detail.delete()
            return JsonResponse({'success': True, 'id': detail_id, 'message': 'Detail deleted successfully'})

        # Handling create
        else:
            form = FinancialDetailForm(request.POST)
            if form.is_valid():
                financial_detail = form.save(commit=False)
                financial_detail.post = post
                financial_detail.save()
                return JsonResponse({
                    'success': True,
                    'id': financial_detail.id,
                    'holding_title': financial_detail.holding_title,
                    'holding_pounds': financial_detail.holding_pounds,
                    'holding_shillings': financial_detail.holding_shillings,
                    'holding_pence': financial_detail.holding_pence,
                    'total_lsd': financial_detail.total_lsd,
                    'message': 'Detail created successfully'
                })
            else:
                logger.error(f"Invalid form for creation: {form.errors}")
                return JsonResponse({'success': False, 'message': 'Form is invalid'})

    else:
        form = FinancialDetailForm()

    # Fetch financial details for the post
    financial_details = post.financial_details.all()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
        'financial_details': financial_details
    })

@csrf_exempt
def update_financial_detail(request):
    if request.method == 'POST':
        detail_id = request.POST.get('detail_id')
        logger.debug(f"Detail ID for update: {detail_id}")
        
        # Check if the detail ID exists and is valid
        if not detail_id:
            return JsonResponse({'success': False, 'message': 'Detail ID is missing'})

        try:
            detail = get_object_or_404(FinancialDetail, id=detail_id)
        except FinancialDetail.DoesNotExist:
            logger.error(f"FinancialDetail with ID {detail_id} not found.")
            return JsonResponse({'success': False, 'message': 'Detail not found'})

        form = FinancialDetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            # Returning updated detail as JSON response for DOM update
            return JsonResponse({
                'success': True,
                'id': detail.id,
                'holding_title': detail.holding_title,
                'holding_pounds': detail.holding_pounds,
                'holding_shillings': detail.holding_shillings,
                'holding_pence': detail.holding_pence,
                'total_lsd': detail.total_lsd,
                'message': 'Detail updated successfully'
            })
        else:
            logger.error(f"Invalid form for update: {form.errors}")
            return JsonResponse({'success': False, 'message': 'Form is invalid'})

@csrf_exempt
def delete_financial_detail(request):
    if request.method == 'POST':
        detail_id = request.POST.get('detail_id')
        if not detail_id:
            return JsonResponse({'success': False, 'message': 'Detail ID is missing'})

        try:
            detail = get_object_or_404(FinancialDetail, id=detail_id)
            detail.delete()
            return JsonResponse({'success': True, 'message': 'Detail deleted successfully', 'id': detail_id})
        except FinancialDetail.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Detail not found'})
    

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
