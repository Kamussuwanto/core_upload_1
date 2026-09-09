# /home/kamusc/myproject/core/models.py
"""
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        # Dictates how the object presents itself in the Admin Panel list
        return self.title
"""
# /home/kamusc/myproject/core/models.py
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # New Field: Uploads files directly to a 'submissions/' subfolder inside your media root
    image = models.ImageField(upload_to='submissions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
