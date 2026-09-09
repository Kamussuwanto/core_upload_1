# /home/kamusc/myproject/core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Import pagination helpers
from .models import Item
from .forms import ItemSubmissionForm

def home_view(request):
    if request.method == 'POST':
        form = ItemSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.is_published = False
            new_item.save()
            messages.success(request, "Thank you for your submission! It will appear once approved.")
            return redirect('home')
    else:
        form = ItemSubmissionForm()

    # 1. Fetch data with memory optimizations intact
    all_items = Item.objects.filter(is_published=True).order_by('-created_at').values('title', 'description', 'image', 'created_at')

    # 2. Initialize Paginator to display 5 items per page
    paginator = Paginator(all_items, 5)

    # 3. Pull the active target page number from URL arguments (?page=2)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page argument is missing or not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page number is out of bounds, deliver the final last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'items': page_obj,  # Pass the paginated subset to the template loop
    }
    return render(request, 'core/home.html', context)
