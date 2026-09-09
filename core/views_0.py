




"""

# /home/kamusc/myproject/core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messaging framework
from .models import Item
from .forms import ItemSubmissionForm

def home_view(request):
    if request.method == 'POST':
        form = ItemSubmissionForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.is_published = False
            new_item.save()

            # Queue up a success message for the next page load
            messages.success(request, "Thank you for your submission! It will appear on the home page once approved.")

            return redirect('home')
    else:
        form = ItemSubmissionForm()

    items = Item.objects.filter(is_published=True).values('title', 'description', 'created_at')

    context = {
        'items': items,
        'form': form
    }
    return render(request, 'core/home.html', context)
"""
from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messaging framework
from .models import Item
from .forms import ItemSubmissionForm

# /home/kamusc/myproject/core/views.py
# ... keep your imports ...

def home_view(request):
    if request.method == 'POST':
        # Add request.FILES to handle image data payloads
        form = ItemSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.is_published = False
            new_item.save()
            messages.success(request, "Thank you for your submission! It will appear once approved.")
            return redirect('home')
    else:
        form = ItemSubmissionForm()

    # Memory optimization: Pull the image path out alongside fields
    items = Item.objects.filter(is_published=True).values('title', 'description', 'image', 'created_at')

    context = {'items': items, 'form': form}
    return render(request, 'core/home.html', context)




